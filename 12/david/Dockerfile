FROM python:3

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80", "--workers", "4"]