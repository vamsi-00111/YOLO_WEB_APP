FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "fast_api:app", "--host", "0.0.0.0", "--port", "800"]