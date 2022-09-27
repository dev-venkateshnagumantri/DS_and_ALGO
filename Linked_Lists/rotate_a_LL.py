# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
         curr=head
        size=0
        while curr.next!=None:
            size+=1
            curr=curr.next
        size+=1
        if size<k:
            return -1
        elif size==k:
           return head
        end=curr
        start=head
        curr=head
        pre=None
        while k>0:
            pre=curr
            curr=curr.next
            k-=1
        pre.next=None
        res=curr
        end.next=start
        return res



#{ 
 # Driver Code Starts
# driver

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = Solution().rotate(lis.head,k)
        printList(head)
# } Driver Code Ends