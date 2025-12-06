FROM alpine:latest AS builder

WORKDIR /docs

RUN apk add python3

RUN apk add py3-pip

COPY /documentation/requirements.txt /docs/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

COPY /documentation/ /docs/documentation

RUN mkdocs build -f /docs/documentation/mkdocs.yml


FROM nginx:alpine

COPY --from=builder /docs/documentation/site /usr/share/nginx/html/
EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]

