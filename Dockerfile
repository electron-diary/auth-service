FROM python:3.12.6

COPY . ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && chmod +x scripts/run_migrations.sh \
    && chmod +x scripts/fastapi_application.sh \
    && chmod +x scripts/faststream_application.sh

WORKDIR /src
