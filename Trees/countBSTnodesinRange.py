class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None

def countBST(root,low,high):
    if not root:
        return 0
    if low<=root.data and root.data<=high:
        return countBST(root.left,low,high)+countBST(root.right,low,high)+1
    else:
        return countBST(root.left,low,high)+countBST(root.right,low,high)

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
ans = countBST(root,15,45)
print(ans)
