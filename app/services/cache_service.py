import json
import redis
from typing import Optional
from app.config import settings

try:
    redis_client = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        decode_responses=True
    )
except Exception:
    redis_client = None


def get_product_from_cache(product_id: str) -> Optional[dict]:
    if not redis_client:
        print("⚠️ Redis client not available")
        return None

    try:
        data = redis_client.get(product_id)

        if data:
            print(f"✅ CACHE HIT: {product_id}")
            return json.loads(data)
        else:
            print(f"❌ CACHE MISS: {product_id}")

    except Exception as e:
        print(f"⚠️ Redis error: {e}")

    return None

def set_product_in_cache(product: dict):
    if not redis_client:
        return
    try:
        redis_client.setex(
            product["id"],
            settings.CACHE_TTL_SECONDS,
            json.dumps(product)
        )
    except Exception:
        pass


def invalidate_product_cache(product_id:

 str):
    if not redis_client:
        return

    try:
        redis_client.delete(product_id)
        print(f"🗑️ CACHE INVALIDATED: {product_id}")
    except Exception as e:
        print(f"⚠️ Redis delete error: {e}")