import redis
import os

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=6379,
    password=os.getenv("REDIS_PASSWORD"),
    ssl=True
)