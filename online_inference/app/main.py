from fastapi import FastAPI, status
from typing import List, Union
import schemas, crud
import uvicorn

app = FastAPI()

@app.get("/health")
def health():
    return {"message" : "drugs"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")