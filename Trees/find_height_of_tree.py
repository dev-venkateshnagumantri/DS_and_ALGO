class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None
def find_height(root):
    if not root:
        return 0
    else:
        return max(find_height(root.left),find_height(root.right))+1


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
print(find_height(root))
