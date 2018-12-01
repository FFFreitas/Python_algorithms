class Node:                
    ...:     def __init__(self, data):
    ...:         self.right = None           
    ...:         self.left = None            
    ...:         self.data = data   
    ...:         self.count = 0


def inorder(root):         
    ...:     if root:                 
    ...:         inorder(root.left)          
    ...:         print(root.data, root.count)
    ...:         inorder(root.right)


def insert(node, data):    
    ...:     if node is None:         
    ...:         return Node(data)           
    ...:                                     
    ...:     if data == node.data:  
    ...:         node.count += 1                       
    ...:         return node       
    ...:                                                 
    ...:     if data < node.data:                   
    ...:         node.left = insert(node.left, data)
    ...:     else:                                    
    ...:         node.right = insert(node.right, data)
    ...:     return node


def deletnode(root, data): 
    ...:     if root is None:         
    ...:         return root                 
    ...:                                     
    ...:     if data < root.data:   
    ...:         root.left = deletnode(root.left, data)
    ...:     elif data > root.data:
    ...:         root.right = deletnode(root.right, data)
    ...:     else:                                  
    ...:         if root.count > 0:                 
    ...:             root.count -= 1                  
    ...:             return root                      
    ...:                                  
    ...:         if root.count == 0:      
    ...:             if root.left is None:
    ...:                 temp = root.right
    ...:                 root = None         
    ...:                 return temp     
    ...:             elif root.right is None:
    ...:                 temp = root.left
    ...:                 root = None
    ...:                 return temp            
    ...:                                  
    ...:             temp = minValue(root.right)                  
    ...:             root.data = temp.data
    ...:             root.right = deletnode(root.right, temp.data)
    ...:             
    ...:     return root    
    ...: 


