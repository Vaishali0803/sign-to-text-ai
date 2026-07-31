import joblib
import numpy as np

class ASLRecognizer:
    def __init__(self):
        self.model = joblib.load("model.pkl")

    def predict(self, features):
        features = np.array(features).reshape(1, -1)

        prediction = self.model.predict(features)[0]
        confidence = self.model.predict_proba(features)[0].max()

        return prediction, confidence