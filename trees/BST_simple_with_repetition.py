class Node:            
    ...:     def __init__(self, data):                      
    ...:         self.left = None       
    ...:         self.right = None           
    ...:         self.data = data                     
    ...:         self.count = 0            
    ...:                               

def inorder(root):     
    ...:     if root:                                       
    ...:         inorder(root.left)     
    ...:         print(root.data, root.count)
    ...:         inorder(root.right)                  
    ...:                               

def insert(root, node):
    ...:     if root is None:                               
    ...:         root = node            
    ...:     elif root.data == node.data:    
    ...:         root.count += 1                      
    ...:     else:                         
    ...:         if root.data < node.data:            
    ...:             if root.right is None:                               
    ...:                 root.right = node             
    ...:             else:
    ...:                 insert(root.right,node)
    ...:         else:                   
    ...:             if root.left is None:
    ...:                 root.left = node       
    ...:             else:               
    ...:                 insert(root.left, node)

