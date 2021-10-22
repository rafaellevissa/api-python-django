FROM python:3
ENV PYTHONUNBUFFERED=1
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT python3 manage.py runserver --settings=app.settings.production 0.0.0.0:8000 && python3 manage.py makemigrations && python3 manage.py migrate
EXPOSE 8000