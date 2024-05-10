FROM python:3

#RUN apt-get update -y && apt-get install -y python3-pip python-dev

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY .  .

EXPOSE 5000

CMD ["python", "extract_kafka_event.py"]
