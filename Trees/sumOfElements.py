class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None
def solvesum(root):
    if not root:
        return 0
    else:
        return root.data+solvesum(root.left)+solvesum(root.right)
def solve(root):
    ans = solvesum(root)
    return ans
#drivercode
root = node(10)
root.left = node(20)
root.right = node(30)
root.left.left = node(1)
root.left.right = node(2)
root.right.left = node(15)
root.right.right = node(25)
print(solve(root))
