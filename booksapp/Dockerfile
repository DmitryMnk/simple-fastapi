#booksapp/Dockerfile
FROM python:3.12

WORKDIR /booksapp
COPY booksapp/pyproject.toml booksapp/poetry.lock* ./

RUN pip install -U pip
RUN pip install poetry

RUN poetry install --no-root

COPY . .

CMD poetry run uvicorn main:app --host 0.0.0.0 --port 8021 --reload
