def good_fibonaci(n):
   ...:     if n <= 1:
   ...:         return (n,0)
   ...:     else:
   ...:         (a,b) = good_fibonaci(n-1)
   ...:         return (a+b,a)

