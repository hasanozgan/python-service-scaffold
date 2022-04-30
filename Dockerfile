FROM python:3.9.9-slim-buster
# ARG PIP_REGISTRY

WORKDIR /code

RUN pip install -U pip
RUN pip install -U poetry
ENV POETRY_VIRTUALENVS_CREATE=false


COPY . .
RUN poetry install
CMD [ "user-cli" ]