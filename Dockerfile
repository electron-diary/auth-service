FROM python:3.12.6

WORKDIR .

COPY . ./

RUN pip install poetry && poetry install --no-dev
RUN chmod +x scripts/run_migrations.sh
RUN chmod +x scripts/fastapi_application.sh
RUN chmod +x scripts/faststream_application.sh
RUN cd /src/