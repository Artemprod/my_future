FROM python:3.10-slim

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN apt-get update && apt-get install -y --no-install-recommends make curl \
    && apt-get install nano && apt-get install -y micro  \
    && apt-get clean

RUN pip install --no-cache-dir poetry==1.7.1

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . ./

ENTRYPOINT ["poetry", "run"]

CMD ["python", "main.py"]