FROM python:3.13.2-bullseye
WORKDIR /app
COPY . /app
RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]
