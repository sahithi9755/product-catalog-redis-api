import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_PORT = int(os.getenv("API_PORT", 8080))
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    CACHE_TTL_SECONDS = int(os.getenv("CACHE_TTL_SECONDS", 3600))
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./products.db")

settings = Settings()