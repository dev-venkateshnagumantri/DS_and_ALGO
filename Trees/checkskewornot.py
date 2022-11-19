class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None
#drivercode
def solve(root):
    if root==None:
        return True
    if root.left==None:
        if root.right:
            return solve(root.right)
        else:
            return True
    elif root.right==None:
        if root.left:
            return solve(root.left)
        else:
            return True
    else:
        return False

#drivercode
root = node(10)

root.right = node(30)

root.right.left = node(15)

root.right.left.right = node(255)

print(solve(root))