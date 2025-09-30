class MyHashMap:
  def __init__(self, capacity=10):
    self.capacity = capacity
    self.buckets = [[] for _ in range(self.capacity)]
    self.size = 0
    
  def _hash_function(self, key):
    return hash(key) % self.capacity

  def put(self, key, value):
    index = self._hash_function(key)
    bucket = self.buckets[index]

    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)  
            return

    bucket.append((key, value))
    self.size += 1

  def get(self, key):
    index = self._hash_function(key)
    bucket = self.buckets[index]

    for k, v in bucket:
        if k == key:
            return v
    return None  

  def remove(self, key):
    index = self._hash_function(key)
    bucket = self.buckets[index]

    for i, (k, v) in enumerate(bucket):
        if k == key:
            del bucket[i]
            self.size -= 1
            return True
    return False  

  def sizeMap(self):
    return self.size

  def print(self):
    items = []
    for bucket in self.buckets:
        for k, v in bucket:
            items.append(f"{k}: {v}")
    return "{" + ", ".join(items) + "}"

  
