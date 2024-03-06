FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1
ENV POSTGRES_PASSWORD jayendra1017
ENV POSTGRES_DB postgres

# Install PostgreSQL client
# RUN apt-get update && \
#     apt-get install -y postgresql-client && \
#     rm -rf /var/lib/apt/lists/*

# WORKDIR /code

COPY . .

RUN apt-get update && \
    apt-get install -y \
        gcc \
        gettext \
        libpq-dev \
        libpcre3 \
        libpcre3-dev \
        zlib1g-dev \
        libjpeg-dev \
        libpng-dev \
        libfreetype6-dev \
        libssl-dev \
        libffi-dev \
        && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements file separately to leverage Docker cache
# COPY requirements.txt /code/requirements.txt

# Install Python dependencies with verbose output
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
