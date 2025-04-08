import redis
import hashlib
import json
from functools import wraps
from typing import Callable

# Setup Redis connection
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

def redis_cache(ttl_seconds: int = 3600):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create a unique key based on args/kwargs
            key_raw = f"{func.__name__}:{args}:{kwargs}"
            key_hash = hashlib.sha256(key_raw.encode()).hexdigest()
            cached = r.get(key_hash)

            if cached:
                return json.loads(cached)

            # Call the actual function
            result = func(*args, **kwargs)

            # Store result in Redis
            r.setex(key_hash, ttl_seconds, json.dumps(result))
            return result

        return wrapper
    return decorator
