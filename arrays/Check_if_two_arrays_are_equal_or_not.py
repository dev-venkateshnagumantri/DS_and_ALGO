class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        if len(A)==len(B):
            dic1=dict()
            for i in A:
                if i not in dic1:
                    dic1[i]=1
                else:
                    dic1[i]+=1
            dic2=dict()
            for j in B:
                if j not in dic2:
                    dic2[j]=1
                else:
                    dic2[j]+=1
            for k in dic1.keys():
                if k not in dic2.keys() or dic1[k]!=dic2[k]:
                    return False
            return True
        else:
            return False
#drivercode
obj = Solution()
N=5
arr1 = [1,2,5,4,0]
arr2 = [2,4,5,0,2]
flag = obj.check(arr1,arr2,N)
print(flag)

                    
        
        
