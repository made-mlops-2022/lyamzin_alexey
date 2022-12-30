from app import schemas
from sklearn.pipeline import Pipeline
from fastapi import status, HTTPException
import pandas as pd
from typing import Union, Optional


def get_pandas_dataframe(test: schemas.Dataset) -> pd.DataFrame:
    return pd.DataFrame(test.dict()["test_objects"])


def get_predictions(
    test: schemas.Dataset, pipeline: Optional[Pipeline]
) -> schemas.Predictions:
    if pipeline is None:
        raise HTTPException(status_code=503, detail="Model unavailable!")
    test_df = get_pandas_dataframe(test)
    predictions = pipeline.predict(test_df)
    return schemas.Predictions(predictions=list(predictions))
