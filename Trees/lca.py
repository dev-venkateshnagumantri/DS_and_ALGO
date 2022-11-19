class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None

def lca(root,v1,v2):
    if not root:
        return
    else:
        if root.data==v1 or root.data==v2:
            return root
        left = lca(root.left,v1,v2)
        right = lca(root.right,v1,v2)
        if left and right:
            return root.data
        elif left:
            return left
        elif right:
            return right
    return None

#drivercode
root = node(10)
root.left = node(20)
root.right = node(30)
root.left.left = node(1)
root.left.right = node(2)
root.right.left = node(15)
root.right.right = node(25)
root.right.right.right = node(255)
root.left.right.left = node(123)
root.left.right.left.right = node(441)
print(lca(root,15,255))