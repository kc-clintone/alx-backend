#!/usr/bin/env python3
"""
MRU (Most Recently Used) cache
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache implements a caching system using
    MRU (Most Recently Used) algorithm.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adding an item in the cache with MRU replacement policy.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Getting an item using key.
        """
        return self.cache_data.get(key, None)
