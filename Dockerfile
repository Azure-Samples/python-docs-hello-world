FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

ENV LISTEN_PORT=8000
EXPOSE 8000

COPY /app /app