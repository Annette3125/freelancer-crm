FROM python:3.12-slim

WORKDIR /app

# Kad nekurti .pyc ir kad logai eitu tiesiai į stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# update pip and install requirements
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy all project
COPY . /app/


# Paleidžiam Django serverį konteineryje
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
