from queue import MyQueue
from stack import MyStack
from hash import MyHashMap


if __name__ == "__main__":
  queue = MyQueue()
  print(f"Is queue empty? {queue.isEmpty()}") 

  queue.enqueue("Apple")
  queue.enqueue("Banana")
  queue.enqueue("Cherry")
  queue.print()

  print(f"Queue size: {queue.size()}") 
  print(f"Front of queue: {queue.peek()}")

  print(f"Dequeued item: {queue.dequeue()}") 
  print(f"Dequeued item: {queue.dequeue()}") 

  queue.enqueue("Date")
  print(f"Queue size: {queue.size()}")
  print(f"Front of queue: {queue.peek()}") 

  print(f"Dequeued item: {queue.dequeue()}") 
  print(f"Dequeued item: {queue.dequeue()}")
  print(f"Is queue empty? {queue.isEmpty()}") 

  try:
      queue.dequeue()
  except IndexError as e:
      print(f"Error: {e}") 

  try:
    queue.peek()
  except IndexError as e:
    print(f"Error: {e}") 
  
  print("___________________________________________________")
  
  stack = MyStack()
  print(f"Is stack empty initially? {stack.isEmpty()}") # True
  
  stack.push(10)
  stack.push(20)
  stack.push(30)
  print(f"Stack after pushes:") 
  stack.print()
  
  print(f"Top element (peek): {stack.peek()}") 
  print(f"Stack size: {stack.size()}") 
  
  popped_item = stack.pop()
  print(f"Popped item: {popped_item}") 
  print(f"Stack after pop:") 
  stack.print()
  
  print(f"Is stack empty now? {stack.isEmpty()}") # False
  
  stack.pop()
  stack.pop()
  print(f"Stack after all pops:") 
  stack.print()
  print(f"Is stack empty after all pops? {stack.isEmpty()}") # True
  
  try:
      stack.pop()
  except IndexError as e:
    print(f"Error: {e}") 
  try:
    stack.peek()
  except IndexError as e:
    print(f"Error: {e}") 

  print("___________________________________________________")

  my_map = MyHashMap()
  my_map.put("apple", 10)
  my_map.put("banana", 20)
  my_map.put("cherry", 30)
  my_map.put("apple", 15) 

  print(f"Value of 'banana': {my_map.get('banana')}")
  print(f"Value of 'apple': {my_map.get('apple')}")
  print(f"Value of 'grape': {my_map.get('grape')}")

  print(f"Map size: {my_map.sizeMap()}")
  print(f"Map content: {my_map.print()}")

  my_map.remove("banana")
  print(f"Map after removing 'banana': {my_map.print()}")
  print(f"Map size after removal: {my_map.sizeMap()}")
