FROM python:3.12.0a5-alpine3.17

ENV POETRY_VERSION=1.3.2

RUN apk add --no-cache \
        curl \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev

RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN poetry install --no-root

COPY ./src /code/src

CMD [ "poetry", "run", "uvicorn", "src.main:app", "--reload","--host","0.0.0.0" ]