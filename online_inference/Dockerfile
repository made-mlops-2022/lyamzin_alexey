FROM python:3.8-slim-buster

WORKDIR /online_inference

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY /app ./app
EXPOSE 8000
RUN chmod +x app/main.py
CMD ["python", "app/main.py", "--port", "8000"]