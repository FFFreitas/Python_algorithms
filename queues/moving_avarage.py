from collections import deque

In [2]: import itertools

In [3]: def movingAvarage(iterable, n=3):
   ...:     it = iter(iterable)
   ...:     d = deque(itertools.islice(it, n-1))
   ...:     d.appendleft(0)
   ...:     s = sum(d)
   ...:     for elem in it:
   ...:         s += elem - d.popleft()
   ...:         d.append(elem)
   ...:         yield s/float(n)
   ...:         

In [4]: arr = [40, 30, 50, 46, 39, 44]

for i in movingAvarage(arr):
   ...:     print i

