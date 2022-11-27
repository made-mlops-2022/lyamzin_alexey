from fastapi.testclient import TestClient
from fastapi import status, HTTPException
import unittest
import app.schemas as schemas
import json

from app.main import app, startup_event


class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        startup_event()

    def setUp(self):
        self.client = TestClient(app)

    def test_predict_positive(self):
        test_dataset = schemas.Dataset(
            test_objects=[
                schemas.TestObject(
                    age=1,
                    sex=1,
                    trestbps=1,
                    chol=1,
                    fbs=1,
                    restecg=1,
                    thalach=1,
                    exang=1,
                    oldpeak=1,
                    slope=1,
                    cp=1,
                    ca=1,
                    thal=1,
                )
            ]
        )

        response = self.client.post("/predict", data=test_dataset.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"predictions": [1]})

    def test_predict_negative_age(self):
        test_json = json.dumps(
            {
                "test_objects": [
                    {
                        "age": 1222,
                        "sex": 0,
                        "cp": 0,
                        "trestbps": 0,
                        "chol": 1,
                        "fbs": 0,
                        "restecg": 0,
                        "thalach": 0,
                        "exang": 0,
                        "oldpeak": 0,
                        "slope": 0,
                        "ca": 0,
                        "thal": 0,
                    }
                ]
            }
        )

        response = self.client.post("/predict", data=test_json)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"detail": "Age should be in range [1, 150]"})

    def test_predict_negative_chol(self):
        test_json = json.dumps(
            {
                "test_objects": [
                    {
                        "age": 1,
                        "sex": 0,
                        "cp": 0,
                        "trestbps": 0,
                        "chol": -2,
                        "fbs": 0,
                        "restecg": 0,
                        "thalach": 0,
                        "exang": 0,
                        "oldpeak": 0,
                        "slope": 0,
                        "ca": 0,
                        "thal": 0,
                    }
                ]
            }
        )
        response = self.client.post("/predict", data=test_json)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {
                "detail": "Chol, thalach, oldpeak and trestbps should be strictly positive"
            },
        )
