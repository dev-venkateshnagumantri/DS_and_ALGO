
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        result = 0
        left = [0 for i in range(n)]
        left[0] = arr[0]
        right = [0 for i in range(n)]
        right[n-1] = arr[n-1]
        for i in range(1,n):
            left[i] = max(left[i-1],arr[i])
        
        for j in range(n-2,-1,-1):
            right[j] = max(right[j+1],arr[j])
        
        for k in range(n):
            result += (min(left[k],right[k]) - arr[k])
        return result
#drivercode
obj = Solution()
arr=[2, 4, 1, 3, 5]
N=5
print(obj.trappingWater(arr,N))