FROM ubuntu:latest
MAINTAINER Elena Hardon
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /backend
WORKDIR /backend
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["./backend/backend.py"]