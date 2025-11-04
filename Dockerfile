FROM python:3.13-slim
COPY docker-flask.py .
COPY requirements-with-text.txt .
RUN pip install --upgrade pip
RUN pip3 install -r requirements-with-versions.txt 
CMD ["python3", "docker-flask.py"]
