import json
from typing import List, Literal
from pydantic import BaseModel, validator
from fastapi import HTTPException, status


class Predictions(BaseModel):
    predictions: List[int]


class TestObject(BaseModel):
    age: int
    sex: Literal[0, 1]
    cp: Literal[0, 1, 2, 3]
    trestbps: int
    chol: int
    fbs: Literal[0, 1]
    restecg: Literal[0, 1, 2]
    thalach: int
    exang: Literal[0, 1]
    oldpeak: float
    slope: Literal[0, 1, 2]
    ca: Literal[0, 1, 2, 3]
    thal: Literal[0, 1, 2]

    @validator("age")
    def age_validator(cls, value):
        if value > 150 or value <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Age should be in range [1, 150]",
            )
            raise ValueError("Age should be strictly positive (ages)")
        return value

    @validator("chol", "thalach", "oldpeak", "trestbps")
    def chol_validator(cls, value):
        if value < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Chol, thalach, oldpeak and trestbps should be strictly positive",
            )
        return value


class Dataset(BaseModel):
    test_objects: List[TestObject]
