class MyStack():
  def __init__(self):
    self._items = []

  def push(self, item):
    self._items.append(item)

  def pop(self):
    if not self.isEmpty():
      return self._items.pop()
    else:
      raise IndexError("Pop from empty stack") 

  def peek(self):
    if not self.isEmpty():
      return self._items[-1]
    else:
      raise IndexError("Peek from empty stack") 

  def isEmpty(self):
    return len(self._items) == 0

  def size(self):
    return len(self._items)

  def print(self):
    print("[",end="")
    if not self.isEmpty():
      print(self._items[-1], "<--")
      for i in range(len(self._items)-2,0,-1):
        print(self._items[i])
      print(self._items[0],end="")

    print("]")