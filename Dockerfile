# Descargar Python 3.11
FROM python:3.11.4-slim-buster

# Establecer el directorio base
WORKDIR /usr/src/django

# Establecer las variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar Depencencias
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copiar el proyecto
COPY . .