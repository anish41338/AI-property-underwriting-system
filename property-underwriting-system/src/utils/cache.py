from typing import Any, Dict, Optional
from datetime import datetime, timedelta
import threading

class SimpleMemoryCache:
    def __init__(self):
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._lock = threading.Lock()
    
    def set(self, key: str, value: Any, expire_seconds: int = 3600):
        """Set a value in cache with expiration"""
        with self._lock:
            self._cache[key] = {
                'value': value,
                'expires_at': datetime.now() + timedelta(seconds=expire_seconds)
            }
    
    def get(self, key: str) -> Optional[Any]:
        """Get a value from cache"""
        with self._lock:
            if key not in self._cache:
                return None
            
            cache_item = self._cache[key]
            if datetime.now() > cache_item['expires_at']:
                del self._cache[key]
                return None
            
            return cache_item['value']
    
    def delete(self, key: str):
        """Delete a key from cache"""
        with self._lock:
            self._cache.pop(key, None)
    
    def clear(self):
        """Clear all cache"""
        with self._lock:
            self._cache.clear()

# Global cache instance
memory_cache = SimpleMemoryCache()
