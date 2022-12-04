FROM python:3.8

RUN mkdir /buid/
COPY requirements.txt /build/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /build/requirements.txt

COPY evaluate_model.py /

ENTRYPOINT [ "python", "evaluate_model.py" ]
