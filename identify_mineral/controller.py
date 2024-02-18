from tensorflow.keras.preprocessing import image
# import cv2
import numpy as np
from .apps import IdentifyMineralConfig


IMG_WIDTH = 150
IMG_HEIGHT = 150
model = IdentifyMineralConfig.loaded_model
labels = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8', 8: '9'}

def predict_mineral(image_path):
    new_img = image.load_img(image_path, target_size=(IMG_WIDTH, IMG_HEIGHT))
    # Use OpenCV to read the image
    # new_img = cv2.imread(image_path)
    # print(new_img)
    # cv2.imshow('image', new_img)
    # # Convert to RGB (OpenCV uses BGR by default)
    # new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB)
    
    # # Resize the image
    # new_img = cv2.resize(new_img, (IMG_WIDTH, IMG_HEIGHT))
    
    # Normalize pixel values
    new_img_array = image.img_to_array(new_img) / 255.0
    new_img_array = np.expand_dims(new_img_array, axis=0)

    # Make predictions using the loaded model
    predictions = model.predict(new_img_array)

    # Decode the predictions to get class labels
    predicted_class = np.argmax(predictions)

    # Map the predicted class to the corresponding label
    predicted_id = labels[predicted_class]
    
    return predicted_id
    