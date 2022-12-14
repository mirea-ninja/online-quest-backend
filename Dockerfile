FROM python:latest

WORKDIR /app/

RUN apt-get update && apt-get install

ENV POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.2.0 \
    POETRY_VIRTUALENVS_CREATE=false

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="$PATH:$POETRY_HOME/bin"

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /app/

RUN bash -c "poetry install --no-root --no-dev"

COPY . /app/

EXPOSE 8080