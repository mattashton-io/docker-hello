FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
RUN ls
RUN pwd
RUN echo "Hi, from Matt"
