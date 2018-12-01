def quicksort(arr,a,b):
   ...:     if a >=b :
   ...:         return
   ...:     pivot = arr[b]
   ...:     left = a
   ...:     right = b -1
   ...:     while left <= right:
   ...:         while left <= right and arr[left] < pivot:
   ...:             left += 1
   ...:         while left <= right and arr[right] > pivot:
   ...:             right -= 1
   ...:             
   ...:         if left <= right:
   ...:             arr[left],arr[right] = arr[right], arr[left]
   ...:             left, right = left+1, right-1
   ...:             
   ...:     arr[left],arr[b] = arr[b],arr[left]
   ...:     quicksort(arr,a,left-1)
   ...:     quicksort(arr,left+1,b)
   ...:     
   ...:     

