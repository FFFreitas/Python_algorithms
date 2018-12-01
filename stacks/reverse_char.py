from collections import deque

def reverse_chr(char):
   ...:     S = deque()
   ...:     original = char
   ...:     reverse = []
   ...:     for i in original:
   ...:         S.append(i)
   ...:         
   ...:     while not len(S) == 0:
   ...:         reverse.append(S.pop())
   ...:         
   ...:     return reverse

