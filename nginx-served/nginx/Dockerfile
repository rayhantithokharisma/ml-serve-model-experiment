FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    nginx \
    build-essential \
    curl \
  && rm -rf /var/lib/apt/lists/*
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 82
CMD ["nginx", "-g", "daemon off;"]