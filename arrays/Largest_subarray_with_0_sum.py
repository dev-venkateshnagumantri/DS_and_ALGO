class Solution:
    def maxLen(self, n, arr):
        #Code here
        dic={}
        sum=0
        maxi=0
        for i in range(n):
            sum = sum+arr[i]
            if arr[i]==0 and maxi==0:
                maxi=1
            if sum==0:
                maxi = i+1
            elif sum in dic.keys():
                maxi = max(maxi,i-dic[sum])
            else:
                dic[sum]=i
        return maxi
#drivercode
obj = Solution()
arr = [15,-2,2,-8,1,7,10,23]
n=len(arr)
print(obj.maxLen(n,arr))
