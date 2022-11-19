def check(matrix,val):
    temp = [0]*len(matrix)
    for i in range(len(matrix)):
        if temp[i]!=matrix[val][i]:
            return False
    return True

def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    return matrix
def solve(matrix):
    mat = transpose(matrix)
    temp = [1]*len(matrix)
    for mark in range(len(mat)):
        flag=False
        for i in range(len(mat[mark])):

            if temp[i]!=mat[mark][i]:
                flag=True
        if flag==False:
            val = mark
            res = check(matrix,val)
            if res:
                return val
    return -1



#driver code
matrix = [[0,0,1,0],
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0]]
print(solve(matrix))
