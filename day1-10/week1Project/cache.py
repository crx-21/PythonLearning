import os
import json
import redis

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "127.0.0.1"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    password=os.getenv("REDIS_PASSWORD", None),
    db=int(os.getenv("REDIS_DB", 0)),
    decode_responses=True,
    protocol=2  # Use RESP2 to avoid "unknown command HELLO" error with older Redis
)

CACHE_TTL = 300 

def get_cached_weather(city: str):
    """Get weather data from cache for a given city."""
    key = f"weather:{city.lower()}"
    data = r.get(key)
    if data:
        return json.loads(data)
    return None

def set_cached_weather(city: str, data: dict, ttl: int = CACHE_TTL):
    """Store weather data in cache with TTL."""
    key = f"weather:{city.lower()}"
    r.setex(key, ttl, json.dumps(data))

def clear_cache(city: str = None):
    """Clear cache for a specific city or all weather keys."""
    if city:
        key = f"weather:{city.lower()}"
        r.delete(key)
    else:
        keys = r.keys("weather:*")
        if keys:
            r.delete(*keys)