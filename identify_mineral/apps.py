import os
from tensorflow.keras.models import model_from_json

from django.apps import AppConfig
from django.conf import settings


class IdentifyMineralConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'identify_mineral'

    # model_json_path = os.path.join(settings.MODEL, 'model.json')
    # model_weights_path = os.path.join(settings.MODEL, 'model_weights.h5')
    model_json_path = os.path.join(settings.MODEL, 'pretrained_model.json')
    model_weights_path = os.path.join(settings.MODEL, 'pretrained_model_weights.h5')
    # Load the model architecture from JSON file
    with open(model_json_path, "r") as json_file:
        loaded_model_json = json_file.read()
    loaded_model = model_from_json(loaded_model_json)

    # Load the model weights
    loaded_model.load_weights(model_weights_path)
