FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3.10 python3.10-dev git

ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 

RUN rm -f /etc/ssl/certs/ca-bundle.crt
RUN apt reinstall -y ca-certificates
RUN update-ca-certificates

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl \
        # deps for building python deps
        build-essential

        RUN curl -sSL https://install.python-poetry.org | python3.10 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app
RUN git clone https://github.com/navkant/book-library.git
WORKDIR book-library
RUN poetry install --no-dev
EXPOSE 8000


CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
