# FROM python:3.11-slim-buster

# ENV PYTHONUNBUFFERED 1
# ENV POSTGRES_PASSWORD jayendra1017
# ENV POSTGRES_DB customer_data_table

# # Install PostgreSQL client
# # RUN apt-get update && \
# #     apt-get install -y postgresql-client && \
# #     rm -rf /var/lib/apt/lists/*

# # WORKDIR /code

# COPY . .

# RUN apt-get update && \
#     apt-get install -y \
#         gcc \
#         gettext \
#         libpq-dev \
#         libpcre3 \
#         libpcre3-dev \
#         zlib1g-dev \
#         libjpeg-dev \
#         libpng-dev \
#         libfreetype6-dev \
#         libssl-dev \
#         libffi-dev \
#         && \
#     rm -rf /var/lib/apt/lists/*

# # Copy requirements file separately to leverage Docker cache
# # COPY requirements.txt /code/requirements.txt

# # Install Python dependencies with verbose output
# RUN pip install -r requirements.txt

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.8-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    gcc \
    libpq-dev \
    libc-dev \
    bash \
    git \
    && pip3 install --upgrade pip


ENV LIBRARY_PATH=/lib:/usr/lib

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


COPY . .

RUN pip3 --no-cache-dir install -r requirements.txt