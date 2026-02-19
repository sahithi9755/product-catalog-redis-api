# ---------- Stage 1: Builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# ---------- Stage 2: Runner ----------
FROM python:3.11-slim

WORKDIR /app

# 🔥 IMPORTANT: copy BOTH lib and bin
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]