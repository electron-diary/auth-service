FROM python:3.12.6

WORKDIR .

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry install --no-dev