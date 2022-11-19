from sys import maxsize
class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None
def check(root,mini,maxi):
    if not root:
        return True
    
    if mini<=root.data and root.data<=maxi:
        flag = check(root.left,mini,root.data-1)
        if flag==False:
            return False
        return check(root.right,root.data+1,maxi)
    else:
        return False
    
    

def checkBST(root):
    mini = -maxsize-1
    maxi = maxsize
    flag = check(root,mini,maxi)
    return flag



#drivercode
root = node(15)
root.left = node(10)
root.right = node(30)
root.left.left = node(5)
root.left.right = node(12)
root.right.right = node(39)

print(checkBST(root))
