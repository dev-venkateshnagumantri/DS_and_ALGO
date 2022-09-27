class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def mergesort(self,arr,count):
        if len(arr)>1:
            mid = len(arr)//2
            L = self.mergesort(arr[:mid],count)
            R = self.mergesort(arr[mid:],count)
            i=j=k=0
            l=len(L)
            r = len(R)
            while i<l and j<r:
                if L[i]>R[j]:
                    arr[k]=R[j]
                    count[0] = count[0]+(l-i)
                    j+=1
                else:
                    arr[k]=L[i]
                    i+=1
                k+=1
            while i<l:
                arr[k]=L[i]
                i+=1
                k+=1
            while j<r:
                arr[k]=R[j]
                j+=1
                k+=1
        return arr
        
    def inversionCount(self, arr, n):
        # Your Code Here
        count = [0]
        self.mergesort(arr,count)
        return count[0]
#drivercode
obj = Solution()
arr=[2, 4, 1, 3, 5]
N=5
print(obj.inversionCount(arr,N))
