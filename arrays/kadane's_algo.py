class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        curr=arr[0]
        max_sum=arr[0]
        for i in range(1,len(arr)):
           curr=max(curr+arr[i],arr[i])
           if curr>max_sum:
               max_sum=curr
               
        return max_sum
#drivercode
obj = Solution()
arr=[1,2,3,-2,5]
N=5
ans=obj.maxSubArraySum(arr,N)
print(ans)
