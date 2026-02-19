from fastapi import FastAPI
from app.api.products import router as product_router
from app.db.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(product_router)


@app.get("/health")
def health():
    return {"status": "ok"}