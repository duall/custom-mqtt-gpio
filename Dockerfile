FROM python:3.8-buster
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "./my-script.py"]
