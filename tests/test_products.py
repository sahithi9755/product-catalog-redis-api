import time
import pytest
import httpx

BASE_URL = "http://api-service:8080"


@pytest.fixture(scope="session")
def client():
    with httpx.Client(base_url=BASE_URL) as c:
        yield c


def create_product(client):
    response = client.post(
        "/products",
        json={
            "name": "Cache Test Product",
            "description": "Testing cache",
            "price": 10.5,
            "stock_quantity": 25,
        },
    )
    assert response.status_code == 201
    return response.json()["id"]


# ✅ Test cache miss then hit
def test_cache_hit_and_miss(client):
    product_id = create_product(client)

    # First GET → MISS (DB fetch)
    r1 = client.get(f"/products/{product_id}")
    assert r1.status_code == 200

    # Small delay to ensure cache set
    time.sleep(0.5)

    # Second GET → HIT (cache)
    r2 = client.get(f"/products/{product_id}")
    assert r2.status_code == 200
    assert r2.json()["id"] == product_id


# ✅ Test cache invalidation on update
def test_cache_invalidation_on_update(client):
    product_id = create_product(client)

    # Populate cache
    client.get(f"/products/{product_id}")

    # Update product
    update_response = client.put(
        f"/products/{product_id}",
        json={"price": 99.99},
    )
    assert update_response.status_code == 200

    # Next GET should still succeed (cache rebuilt)
    r = client.get(f"/products/{product_id}")
    assert r.status_code == 200
    assert r.json()["price"] == 99.99


# ✅ Test delete behavior
def test_delete_product(client):
    product_id = create_product(client)

    # Delete
    d = client.delete(f"/products/{product_id}")
    assert d.status_code == 204

    # Should return 404
    r = client.get(f"/products/{product_id}")
    assert r.status_code == 404