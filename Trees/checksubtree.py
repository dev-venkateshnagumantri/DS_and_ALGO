class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None

def checkidentical(root1,root2):
    if not root1 or not root2:
        return True
    if root1.data!=root2.data:
        return False
    flag = checkidentical(root1.left,root2.left)
    if not flag:
        return False
    flag = checkidentical(root1.right,root2.right)
    if not flag:
        return False
    return True

def checksubtree(T,S):
    if S is None:
        return True
    if T is None:
        return False
    if checkidentical(T,S):
        return True
    else:
        return checksubtree(T.left,S) or checksubtree(T.right,S)

#drivercode
root1 = node(25)
root1.right = node(255)
root1.left = node(245)

root = node(10)
root.left = node(20)
root.right = node(30)
root.left.left = node(1)
root.left.right = node(2)
root.right.left = node(15)
root.right.right = node(25)
root.right.right.right = node(255)
root.right.right.left = node(245)
root.left.right.left = node(123)
root.left.right.left.right = node(441)


print(checksubtree(root,root1))