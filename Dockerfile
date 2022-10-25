FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=8000

WORKDIR /app

RUN pip install --upgrade pip

COPY ./app/templates /app/templates

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app
