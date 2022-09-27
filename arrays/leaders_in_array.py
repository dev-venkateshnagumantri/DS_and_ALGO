class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        maxi=-1
        a=A[::-1]
        lead=[]
        for i in a:
            if i>=maxi:
                maxi=i
                lead.append(i)
        return lead[::-1]
#drivercode
obj = Solution()
n = 6
A = [16,17,4,3,5,2]
print(obj.leaders(A,n))
