
import sys
class Solution:
    def maximumSumRectangle(self,R,C,M):
        #code here
        r,c=R,C
        max_sum=-sys.maxsize-1
        for i in range(c):
            arr=[0 for x in range(r)]
            for j in range(i,c):
                
                for k in range(r):
                    arr[k]+=M[k][j]
                #kadane's algorithm for condition all -ve numbers
                curr_sum=0
                for p in range(0,r):
                    curr_sum=max(arr[p],curr_sum+arr[p])
                    max_sum=max(max_sum,curr_sum)
        return max_sum 
#drivercode
obj=Solution()
matrix = [[-8,-3,4,2,1],
        [3,8,10,1,3],
        [-4,-1,1,7,-6]]
        
print(obj.maximumSumRectangle(len(matrix),len(matrix[0]),matrix))       