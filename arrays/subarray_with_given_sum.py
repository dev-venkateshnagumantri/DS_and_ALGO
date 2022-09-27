class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        l=0
        r=1
        cur_sum=arr[0]
        if n==0 or min(arr)>s:
            return [-1]
        if cur_sum==s:
            return [l+1,l+1]
        while r<n:
            cur_sum+=arr[r]
            while cur_sum>s:
                cur_sum-=arr[l]
                l+=1
            if cur_sum==s:
                return [l+1,r+1]
            r+=1
        return [-1]
obj = Solution()
arr = [1,2,3,7,5]
s=12
print(obj.subArraySum(arr,len(arr),s))
