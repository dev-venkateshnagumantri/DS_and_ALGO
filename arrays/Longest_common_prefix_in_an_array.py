#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        check=""
        s=arr[0]
        for i in range(len(s)):
            check+=s[i]
            flag=False
            for j in range(1,n):
                if i+1<=len(arr[j]):
                    if check==arr[j][:i+1]:
                        continue
                    else:
                        flag=True
                        break
                else:
                    flag=True
                    break
            if len(check)==1 and flag==True:
                return -1
            elif flag:
                return check[:i]
        return check
#drivercode
obj = Solution()
n = 4
arr = ["sowmya","sowmyaarao", "sow",
         "sowmyabala","gsow"]
print(obj.longestCommonPrefix(arr,n))
