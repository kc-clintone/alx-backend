#!/usr/bin/env python3
"""
LFU (Leas Frequently Used) caching
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache implements a caching system using
    LFU (Least Frequently Used) algorithm with LRU fallback.
    """

    def __init__(self):
        """
        Initializing the cache.
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """
        Adding an item in the cache with LFU replacement policy.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min(self.frequency.values())]

                if len(lfu_keys) > 1:
                    lfu_lru_key = next(k for k in self.usage_order if k in lfu_keys)
                else:
                    lfu_lru_key = lfu_keys[0]

                del self.cache_data[lfu_lru_key]
                del self.frequency[lfu_lru_key]
                self.usage_order.pop(lfu_lru_key)
                print(f"DISCARD: {lfu_lru_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = None

    def get(self, key):
        """
        Getting an item using key.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]

    def print_cache(self):
        """
        Prints the cache content.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")
