from app import schemas
from sklearn.pipeline import Pipeline
from fastapi import status, HTTPException
import pandas as pd
from typing import Union


def get_pandas_dataframe(test: schemas.Dataset) -> pd.DataFrame:
    return pd.DataFrame(test.dict()["test_objects"])


def get_predictions(
    test: schemas.Dataset, pipeline: Union[Pipeline, None]
) -> schemas.Predictions:
    if pipeline is None:
        raise HTTPException(status_code=503, detail="Model unavailable!")
    test_df = get_pandas_dataframe(test)
    predictions = pipeline.predict(test_df)
    return schemas.Predictions(predictions=list(predictions))


def healthcheck(pipeline: Union[Pipeline, None]):
    if pipeline is None:
        return status.HTTP_503_SERVICE_UNAVAILABLE
    dummy_dataset = schemas.Dataset(
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
    try:
        _ = pipeline.predict(pd.DataFrame(dummy_dataset.dict()["test_objects"]))
    except:
        return status.HTTP_503_SERVICE_UNAVAILABLE
    return status.HTTP_200_OK
