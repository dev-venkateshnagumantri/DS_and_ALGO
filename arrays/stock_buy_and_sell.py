class Solution:
    #Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, A, n):
        #code here
        arr = A
        max_p=0
        buyday,sellday = 0,0
        res = []
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                sellday+=1
            else:
                max_p += (arr[sellday]-arr[buyday])
                res.append([buyday,sellday])
                buyday = sellday = i
        max_p += (arr[sellday]-arr[buyday])
        if sellday>buyday:
            res.append([buyday,sellday])
        return res if max_p>0 else []
#drivercode
obj = Solution()
arr=[100,180,260,310,40,535,695]
N=7
print(obj.stockBuySell(arr,N))