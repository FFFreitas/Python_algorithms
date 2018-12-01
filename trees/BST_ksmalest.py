# your task is to complete this function
# function should return kth smallest element from the BST
def storeInorder(root, inorder):
    if root is None:
        return
    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)

def k_smallest_element(root, n):
    # Code here
    temp =[]
    storeInorder(root, temp)
    temp.sort()
    return temp[n-1]
