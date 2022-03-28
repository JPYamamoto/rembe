FROM python:3.10-alpine3.15

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .

RUN apk update
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    postgresql-dev gcc musl-dev libffi libffi-dev
RUN pip install -r ./requirements.txt --no-cache-dir

COPY . .

ARG database_name
ARG database_user
ARG database_pass
ARG database_host
ARG database_port

ENV DATABASE_NAME $database_name
ENV DATABASE_USER $database_user
ENV DATABASE_PASS $database_pass
ENV DATABASE_HOST $database_host
ENV DATABASE_PORT $database_port

RUN python ./manage.py migrate --noinput

EXPOSE 8000
ENTRYPOINT ["./manage.py", "runserver", "0.0.0.0:8000"]
