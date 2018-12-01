1 class ArrayQueue:
2
”””FIFO queue implementation using a Python list as underlying storage.”””
# moderate capacity for all new queues
3
DEFAULT CAPACITY = 10
4
5
def init (self):
6
”””Create an empty queue.”””
7
self. data = [None] ArrayQueue.DEFAULT CAPACITY
8
self. size = 0
9
self. front = 0
10
11
def len (self):
12
”””Return the number of elements in the queue.”””
13
return self. size
14
15
def is empty(self):
16
”””Return True if the queue is empty.”””
17
return self. size == 0
18
19
def first(self):
20
”””Return (but do not remove) the element at the front of the queue.
21
22
Raise Empty exception if the queue is empty.
23
”””
24
if self.is empty( ):
25
raise Empty( Queue is empty )
26
return self. data[self. front]
27
28
def dequeue(self):
29
”””Remove and return the first element of the queue (i.e., FIFO).
30
31
Raise Empty exception if the queue is empty.
32
”””
33
if self.is empty( ):
34
raise Empty( Queue is empty )
35
answer = self. data[self. front]
# help garbage collection
36
self. data[self. front] = None
37
self. front = (self. front + 1) % len(self. data)
38
self. size −= 1
39
return answer

40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
def enqueue(self, e):
”””Add an element to the back of queue.”””
if self. size == len(self. data):
# double the array size
self. resize(2 len(self.data))
avail = (self. front + self. size) % len(self. data)
self. data[avail] = e
self. size += 1
# we assume cap >= len(self)
def resize(self, cap):
”””Resize to a new list of capacity >= len(self).”””
# keep track of existing list
old = self. data
# allocate list with new capacity
self. data = [None] cap
walk = self. front
# only consider existing elements
for k in range(self. size):
# intentionally shift indices
self. data[k] = old[walk]
walk = (1 + walk) % len(old)
# use old size as modulus
# front has been realigned
self. front = 0
