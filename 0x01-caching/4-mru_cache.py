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
        Initializing the cache.
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Adding an item in the cache with MRU replacement policy.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.access_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.access_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """
        Getting an item using key.
        """
        if key is None or key not in self.cache_data:
            return None

        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]

    def print_cache(self):
        """
        Prints the cache content.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")
