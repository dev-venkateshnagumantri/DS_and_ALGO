class Solution:
    def MissingNumber(self,array,n):
        # code here
        array.sort()
        count=1
        for i in range(len(array)):
            if array[i]!=count:
                return count
            count+=1
        return count if count<=n else -1

obj = Solution()
n=5
arr = [1,2,3,5]
print(obj.MissingNumber(arr,n))