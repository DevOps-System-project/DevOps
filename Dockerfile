FROM python:3.14-slim

RUN useradd --create-home appuser

WORKDIR /home/appuser/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/

USER appuser

EXPOSE 8000

CMD ["python", "-m", "app.main"]
