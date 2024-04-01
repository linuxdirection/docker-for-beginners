# Build stage
FROM ubuntu:latest as builder
RUN apt-get update && apt-get install -y nginx
COPY . /var/www/html

# Production stage
FROM nginx:alpine
COPY --from=builder /var/www/html /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
