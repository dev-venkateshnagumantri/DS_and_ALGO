class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None
def solve(root1,root2):
    if not root1 or not root2:
        return True
    if root1.data!=root2.data:
        return False
    flag = solve(root1.left,root2.left)
    if not flag:
        return False
    flag = solve(root1.right,root2.right)
    if not flag:
        return False
    return True



#drivercode
root1 = node(10)
root1.left = node(20)
root1.right = node(30)
root1.left.left = node(1)
root1.left.right = node(2)
root1.right.left = node(15)
root1.right.right = node(25)
root2 = node(10)
root2.left = node(20)
root2.right = node(30)
root2.left.left = node(1)
root2.left.right = node(2)
root2.right.left = node(15)
root2.right.right = node(255)
print(solve(root1,root2))