FROM python:3.7.3-alpine3.8

WORKDIR /app/
COPY *.py *.txt /app/
RUN pip install -r requirements.txt 


CMD ["python", "hello.py"]
