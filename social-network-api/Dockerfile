FROM python:3.12-rc-bullseye

ENV POETRY_VERSION=1.3.2
#RUN apk add gcc g++
RUN pip install poetry

WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN poetry install --no-root

COPY ./src /code/src

CMD [ "poetry", "run", "uvicorn", "src.main:app", "--reload","--host","0.0.0.0" ]