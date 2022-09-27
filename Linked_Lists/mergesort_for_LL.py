#User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def sortmerge(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            L=arr[:mid]
            R=arr[mid:]
            l=self.sortmerge(L)
            r=self.sortmerge(R)
            i=j=k=0
            while i<len(l) and j<len(r):
                if l[i]<r[j]:
                    arr[k]=l[i]
                    i+=1
                else:
                    arr[k]=r[j]
                    j+=1
                k+=1
            while i<len(l):
                arr[k]=l[i]
                i+=1
                k+=1
            while j<len(r):
                arr[k]=r[j]
                j+=1
                k+=1
        return arr
    
    def mergeSort(self, head):
        a=[]
        curr=head
        while curr!=None:
            a.append(curr.data)
            curr=curr.next
        a=self.sortmerge(a)
        res=Node(a[0])
        temp=res
        i=1
        while i<len(a):
            temp.next=Node(a[i])
            temp=temp.next
            i+=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends