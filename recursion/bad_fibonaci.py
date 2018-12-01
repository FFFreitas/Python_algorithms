def bad_fibonaci(n):
   ...:     if n <= 1:
   ...:         return n
   ...:     else:
   ...:         return bad_fibonaci(n-2) + bad_fibonaci(n-1)

