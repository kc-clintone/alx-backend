#!/usr/bin/env python3
"""
FIFO caching
"""

from base_caching import BaseCaching


class FFOCache(BaseCaching):
    """
    FIFOCache implements a caching system using
    FIFO (First-In, First-Out) algorithm.
    """

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache with FIFO replacement policy.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first_key = self.order.pop(0)
                    del self.cache_data[first_key]
                    print(f"DISCARD: {first_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get an item by key.
        """
        return self.cache_data.get(key, None)
