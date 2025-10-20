FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
# RUN pip3 install flask
# CMD ["python3", "docker-flask.py"]
