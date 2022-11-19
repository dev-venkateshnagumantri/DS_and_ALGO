class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None
def level_order(root):
    if not root:
        return []
    res = []
    q=[]
    temp=[]
    q.append(root)
    q.append(None)
    while q:
        curr = q.pop(0)
        if curr:
            temp.append(curr.data)
        if curr==None:
            res.append(temp)
            if q:
                q.append(None)

                temp = []
            else:
                break
        if curr:
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return res
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
res  = level_order(root)
for i in res:
    print(i)