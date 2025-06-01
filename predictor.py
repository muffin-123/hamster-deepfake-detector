import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

class HamsterDetector:
    def __init__(self, model_path=None):
        if model_path is None:
            model_path = os.path.join(os.path.dirname(__file__), 'mesonet_model.h5')
        self.model = load_model(model_path)

    def predict(self, image_path):
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image could not be read.")
        img = cv2.resize(img, (256, 256))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        pred = self.model.predict(img)[0][0]
        label = "Fake" if pred > 0.5 else "Real"
        return {
            "prediction": label,
            "confidence_fake": round(float(pred), 4),
            "confidence_real": round(1.0 - float(pred), 4)
        }
