FROM python:3.7.3-stretch

WORKDIR /app/
COPY *.py *.txt *.ini /app/
RUN pip install -r requirements.txt 

CMD ["uwsgi", "--ini", "app.ini"]
