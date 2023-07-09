FROM python:3.11.4

WORKDIR /app/bot
COPY bot .

WORKDIR /app

COPY app.py .
COPY .env .
COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
RUN pip cache purge

CMD ["python", "app.py"]
