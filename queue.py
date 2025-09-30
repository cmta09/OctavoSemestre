class MyQueue:

  def __init__(self):
    self._items = []
  
  def enqueue(self, item):
    self._items.append(item)
  
  def dequeue(self):
    if not self.isEmpty():
      return self._items.pop(0)
    else:
      raise IndexError("dequeue from empty queue")
  
  def peek(self):
    if not self.isEmpty():
      return self._items[0]
    else:
      raise IndexError("peek from empty queue")
  
  def isEmpty(self):
    if len(self._items) == 0:
      return True
    else:
      return False
  
  def size(self):
    return len(self._items)
  
  def print(self):
    print("[",end="")
    if not self.isEmpty():
      print(self._items[0], end=" ")
      for i in range(1,len(self._items)-1):
        print(self._items[i], end=" ")
      print(self._items[-1],end="")
  
    print("]")