#!/usr/bin/env python3
"""
LIFO caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache implements a caching system using
    LIFO (Last-In, First-Out) algorithm.
    """

    def __init__(self):
        """
        Initializing the cache.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Adding an item in the cache with LIFO replacement policy.
        """
        if key is not None and item is not None:
            if key not in self.cache_data
            and len(self.cache_data) >= BaseCaching.MAX_ITEMS:

                if self.last_key:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """
        Getting an item using key.
        """
        return self.cache_data.get(key, None)
