class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None
    
def solve(root):
    if not root:
        return 1
    if not root.left and not root.right:
        return 1
    if root.left and root.right:
        return (solve(root.left) and solve(root.right))
    return 0

#drivercode
root = node(10)
root.left = node(20)
root.right = node(30)
root.left.left = node(1)
root.left.right = node(2)



print(solve(root))
