def is_matche(expr):
   ...:     lefty = '{[('
   ...:     righty = '}])'
   ...:     S = deque()
   ...:     for c in expr:
   ...:         if c in lefty:
   ...:             S.append(c)
   ...:         elif c in righty:
   ...:             if len(S) == 0:
   ...:                 return False
   ...:             if righty.index(c) != lefty.index(S.pop()):
   ...:                 return False
   ...:     return len(S) == 0

