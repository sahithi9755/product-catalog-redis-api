# 🚀 Product Catalog API with Redis Caching

High-performance backend API for managing a product catalog using the **Cache-Aside pattern with Redis**.
This project demonstrates production-ready caching, containerization, and automated testing.

---

## 📌 Project Overview

Modern read-heavy applications suffer from database bottlenecks.
This service improves performance by introducing **Redis caching** with proper **cache invalidation** to maintain consistency.

### ✨ Key Highlights

* ⚡ FastAPI REST backend
* 🧠 Cache-Aside caching strategy
* 🔥 Redis distributed cache
* ⏳ Configurable TTL
* 🐳 Fully Dockerized stack
* ✅ Automated integration tests
* 🛡️ Graceful Redis failure handling
* 📦 Clean production-style architecture

---

## 🏗️ Architecture

```
Client → FastAPI → Redis Cache → Database (SQLite)
```

### 🔄 Read Flow

1. Check Redis cache
2. If HIT → return fast
3. If MISS → query DB
4. Store in Redis with TTL
5. Return response

### ✏️ Write Flow

1. Update database
2. Invalidate cache
3. Next read repopulates cache

---

## 📂 Project Structure

```
product-catalog/
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── db/
│   ├── config.py
│   └── main.py
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Environment Variables

See `.env.example`

| Variable          | Description         | Default |
| ----------------- | ------------------- | ------- |
| API_PORT          | API listening port  | 8080    |
| REDIS_HOST        | Redis hostname      | redis   |
| REDIS_PORT        | Redis port          | 6379    |
| CACHE_TTL_SECONDS | Cache expiry        | 3600    |
| DATABASE_URL      | Database connection | SQLite  |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/product-catalog-redis-api.git
cd product-catalog-redis-api
```

---

### 2️⃣ Run with Docker

```bash
docker-compose up --build
```

---

### 3️⃣ Health Check

```
GET http://localhost:8080/health
```

Expected:

```json
{"status": "ok"}
```

---

## 📡 API Endpoints

### 🔹 Create Product

```
POST /products
```

**Request**

```json
{
  "name": "Example Product",
  "description": "A detailed description",
  "price": 29.99,
  "stock_quantity": 100
}
```

**Response:** `201 Created`

---

### 🔹 Get Product

```
GET /products/{id}
```

**Responses**

* `200 OK` — found
* `404 Not Found` — missing

---

### 🔹 Update Product

```
PUT /products/{id}
```

**Response:** `200 OK`

---

### 🔹 Delete Product

```
DELETE /products/{id}
```

**Response:** `204 No Content`

---

## 🔥 Cache Behavior Demonstration

The application logs clearly show cache activity:

```
❌ CACHE MISS: <id>
✅ CACHE HIT: <id>
🗑️ CACHE INVALIDATED: <id>
```

### ✅ Verified Scenarios

* Cache miss on first read
* Cache hit on subsequent read
* Cache invalidation on update
* Cache invalidation on delete
* Graceful fallback if Redis fails

---

## 🧪 Running Tests

```bash
docker-compose exec api-service pytest tests/
```

Example output:

```
3 passed in 0.72s
```

---

## 📸 Screenshots

> *(Add your screenshots here for full marks)*

Recommended:

* POST success
* Cache MISS log
* Cache HIT log
* Cache INVALIDATED log
* Pytest passing

---

## 🎯 Design Decisions

* **Cache-Aside** chosen for explicit control
* **TTL** prevents stale data buildup
* **Invalidate on write** ensures consistency
* **Docker Compose** enables reproducible environment
* **SQLite** kept simple to focus on caching layer

---

## 🚧 Error Handling

The service gracefully handles:

* Redis unavailable → falls back to DB
* Invalid input → 400 responses
* Missing product → 404 responses
* Internal errors → 500 responses

---

## 🏆 Production Considerations

This project demonstrates:

* Stateless API design
* Proper HTTP status usage
* Containerized deployment
* Config-driven settings
* Testable architecture
* Scalable caching strategy

---

## 🔮 Future Improvements

* Async Redis client
* Connection pooling tuning
* Pagination & product listing
* Prometheus metrics
* Load testing
* PostgreSQL support

---

## 👩‍💻 Author

**Sahithi**

---

## 📜 License

This project is for educational and demonstration purposes.

---
