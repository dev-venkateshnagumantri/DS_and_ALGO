class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None

def solve(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.data
    return solve(root.left)+solve(root.right)


#drivercode
root = node(10)
root.left = node(20)
root.right = node(30)
root.left.left = node(1)
root.left.right = node(2)
root.right.left = node(15)
root.right.right = node(25)
print(solve(root))