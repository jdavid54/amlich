# queue https://www.geeksforgeeks.org/queue-in-python/

# 1 - list
# Python program to
# demonstrate queue implementation
# using list
print('=================== 1 using list')
# Initializing a queue
queue = []
 
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
 
print("Initial queue")
print(queue)
 
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
 
print("\nQueue after removing elements")
print(queue)
 
# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty

# 2 - deque
# Python program to
# demonstrate queue implementation
# using collections.dequeue
 
print('================== 2 using collections.deque module')  
from collections import deque
 
# Initializing a queue
q = deque()
 
# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
 
print("Initial queue")
print(q)
 
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
 
print("\nQueue after removing elements")
print(q)
 
# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty
# q.popleft()

# 3 - using queue module
# Python program to
# demonstrate implementation of
# queue using queue module
 
print('================= 3 using queue module') 
from queue import Queue
 
# Initializing a queue
q = Queue(maxsize = 3)
 
# qsize() give the maxsize
# of the Queue
print(q.qsize())
 
# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
 
# Return Boolean for Full
# Queue
print("\nFull: ", q.full())
 
# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
 
# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())
 
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
 
# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())