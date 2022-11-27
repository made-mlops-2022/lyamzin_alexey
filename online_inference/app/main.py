from app import schemas, crud

# import schemas
# import crud
import uvicorn
import dill
import gdown
import os
from fastapi import FastAPI, status, HTTPException
from sklearn.pipeline import Pipeline


app = FastAPI()
pipeline = None


@app.on_event("startup")
def startup_event():
    gdown.download(
        url=os.environ["TRANSFORMER_LINK"],
        output="models/transformer.dill",
        quiet=False,
        fuzzy=True,
    )
    gdown.download(
        url=os.environ["CLASSIFIER_LINK"],
        output="models/classifier.dill",
        quiet=False,
        fuzzy=True,
    )

    with open("models/transformer.dill", "rb") as file:
        transformer = dill.load(file)
    with open("models/classifier.dill", "rb") as file:
        classifier = dill.load(file)
    global pipeline
    pipeline = Pipeline(
        steps=[("feature_transformer", transformer), ("estimator", classifier)]
    )


@app.get("/health")
def health():
    return crud.healthcheck(pipeline)


@app.post(
    "/predict", response_model=schemas.Predictions, status_code=status.HTTP_200_OK
)
def predict(test: schemas.Dataset):
    # try:
    #     predictions = crud.get_predictions(test, pipeline)
    #     return predictions
    # except HTTPException as err:
    #     raise err
    return crud.get_predictions(test, pipeline)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
