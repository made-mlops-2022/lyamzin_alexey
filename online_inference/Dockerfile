FROM python:3.8-slim-buster

WORKDIR /online_inference

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY /src ./src
ENV PYTHONPATH "${PYTHONPATH}:/"
ENV TRANSFORMER_LINK "https://drive.google.com/file/d/1XHm10etHm7akMvubIKmTwMw8QS1HwjWd/view?usp=sharing"
ENV CLASSIFIER_LINK "https://drive.google.com/file/d/1Nl0SXC3plM-lOQG7Z7T9xET4GRG_EXH0/view?usp=share_link"

COPY /app ./app
RUN mkdir models
EXPOSE 8000
RUN chmod +x app/main.py
CMD ["python", "app/main.py", "--port", "8000"]