from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage
import os

from minerals.settings import MEDIA_ROOT
from .controller import predict_mineral
from PIL import Image
import io


class MineralView(APIView):

    def validate_image(self, image):
        valid_extension = ['jpg', 'png', 'jpeg']
        ext = image.split('.')[-1].lower()
        if ext not in valid_extension:
            return False
        return True
    
    def save_file(self, file):
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_path = f'{MEDIA_ROOT}/{filename}'
        return file_path
    
    def post(self, request):
        try:
            if 'image' not in request.FILES:
                return Response({"message": 'image not provided!'}, status=status.HTTP_400_BAD_REQUEST)
            
            file = request.FILES['image']
            if not self.validate_image(file.name):
                return Response({"message": 'Invalid File!'}, status=status.HTTP_204_NO_CONTENT)
            
            # Save Image
            image_path = self.save_file(file)
            
            # Predict Mineral ID
            id = predict_mineral(image_path)
            if os.path.exists(image_path):
                os.remove(image_path)
            
            return Response(
                {"success": True,
                "data":{
                    "Id": id
                }},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({"success": False,"message":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
