#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here
        top,down,left,right=0,r-1,0,c-1
        di=0
        res=[]
        while top<=down and left<=right:
            if di==0:
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top+=1
            elif di==1:
                for i in range(top,down+1):
                    res.append(matrix[i][right])
                right-=1
            elif di==2:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down-=1
            elif di==3:
                for i in range(down,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
            di=(di+1)%4
        return res
#drivercode
obj = Solution()
matrix = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
r = 3
c = 4
print(obj.spirallyTraverse(matrix,r,c))
