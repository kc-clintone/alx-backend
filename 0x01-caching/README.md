# Caching System

## Overview

This project/repository demonstrates various caching algorithms implemented in Python. The caching systems are built on top of a base caching class, `BaseCaching`, which defines the core structure and functionality of the caching mechanisms. The following caching strategies are implemented:

- **Basic Cache** (No limit)
- **FIFO Cache** (First-In, First-Out)
- **LIFO Cache** (Last-In, First-Out)
- **LRU Cache** (Least Recently Used)
- **MRU Cache** (Most Recently Used)
- **LFU Cache** (Least Frequently Used)

Each caching system inherits from the `BaseCaching` class and implements specific cache replacement policies.

## Project Structure

```
.
├── base_caching.py
├── basic_cache.py
├── fifo_cache.py
├── lifo_cache.py
├── lru_cache.py
├── mru_cache.py
├── lfu_cache.py
└── README.md
```

- **base_caching.py**: Contains the `BaseCaching` class that provides the basic structure for caching systems.
- **basic_cache.py**: Implements the Basic Cache system with no limit on cache size.
- **fifo_cache.py**: Implements the FIFO (First-In, First-Out) caching algorithm.
- **lifo_cache.py**: Implements the LIFO (Last-In, First-Out) caching algorithm.
- **lru_cache.py**: Implements the LRU (Least Recently Used) caching algorithm.
- **mru_cache.py**: Implements the MRU (Most Recently Used) caching algorithm.
- **lfu_cache.py**: Implements the LFU (Least Frequently Used) caching algorithm with LRU fallback.

## Usage

### BaseCaching

The `BaseCaching` class provides the foundational structure for all caching classes. It contains:

- `cache_data`: A dictionary that stores cached items.
- `MAX_ITEMS`: A constant that sets the maximum number of items the cache can hold.
- `print_cache()`: A method to print the current state of the cache.
- `put(key, item)`: Method to add an item to the cache (to be implemented by child classes).
- `get(key)`: Method to retrieve an item from the cache (to be implemented by child classes).

### BasicCache

This caching system does not have any limits. It simply adds items to the cache and retrieves them.

```python
from basic_cache import BasicCache

my_cache = BasicCache()
my_cache.put("A", "Hello")
print(my_cache.get("A"))  # Output: Hello
```

### FIFOCache

This cache follows the First-In, First-Out (FIFO) replacement policy. When the cache is full, the oldest item is discarded.

```python
from fifo_cache import FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.put("E", "Battery")  # "A" will be discarded
```

### LIFOCache

This cache follows the Last-In, First-Out (LIFO) replacement policy. When the cache is full, the most recently added item is discarded.

```python
from lifo_cache import LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.put("E", "Battery")  # "D" will be discarded
```

### LRUCache

This cache follows the Least Recently Used (LRU) replacement policy. When the cache is full, the least recently used item is discarded.

```python
from lru_cache import LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.get("A")  # Access "A" to mark it as recently used
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.put("E", "Battery")  # "B" will be discarded
```

### MRUCache

This cache follows the Most Recently Used (MRU) replacement policy. When the cache is full, the most recently used item is discarded.

```python
from mru_cache import MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.get("B")  # Access "B" to mark it as recently used
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.put("E", "Battery")  # "B" will be discarded
```

### LFUCache

This cache follows the Least Frequently Used (LFU) replacement policy. When the cache is full, the least frequently used item is discarded. If there is a tie, the Least Recently Used (LRU) item is discarded.

```python
from lfu_cache import LFUCache

my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.get("A")  # Access "A" to increase its frequency
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.put("E", "Battery")  # "B" will be discarded (LFU)
```

## Testing

To test each caching strategy, you can run the scripts individually and observe the behavior of the cache as items are added and retrieved.

```bash
python3 basic_cache.py
python3 fifo_cache.py
python3 lifo_cache.py
python3 lru_cache.py
python3 mru_cache.py
python3 lfu_cache.py
```
