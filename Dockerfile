FROM python:3.10-alpine3.15

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /app
WORKDIR /app

RUN pip install -r ./requirements.txt
RUN python ./manage.py migrate --noinput

EXPOSE 8000
ENTRYPOINT ["./manage.py", "runserver", "0.0.0.0:8000"]
