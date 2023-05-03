FROM python:3.11 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11

WORKDIR /service

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONOPTIMIZE=TRUE

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

COPY ./src /service/src

COPY ./alembic.ini /service/alembic.ini

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.ASGI.app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]



