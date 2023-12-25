FROM python:3.9-alpine

WORKDIR /app

COPY . /app

RUN \
    apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        libffi-dev \
        openssl-dev \
        git && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    apk add --no-cache mariadb-dev && \
    poetry install && \
    apk del .build-deps

EXPOSE 8000

CMD ["poetry", "run", "uwsgi"]
