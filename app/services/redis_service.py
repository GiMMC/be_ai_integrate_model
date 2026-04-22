from app.db.redis import redis_client

def set_value(key: str, value: str, ex: int = 3600):
    redis_client.set(key, value, ex=ex)

def get_value(key: str):
    return redis_client.get(key)