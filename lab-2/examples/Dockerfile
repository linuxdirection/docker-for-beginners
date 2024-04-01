FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
COPY . /var/www/html
CMD ["nginx", "-g", "daemon off;"]