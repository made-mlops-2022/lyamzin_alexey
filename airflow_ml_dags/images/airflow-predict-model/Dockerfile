FROM python:3.8

RUN mkdir /buid/
COPY requirements.txt /build/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /build/requirements.txt

COPY predict.py /

ENTRYPOINT [ "python", "predict.py" ]
