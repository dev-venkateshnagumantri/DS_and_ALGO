class Solution:
    def overlappedInterval(self, Intervals):
	    #Code here
        Intervals.sort(key=lambda x:x[0])
        ans=Intervals[0]
        res = []
        n = len(Intervals)
        for i in range(1,n):
            curr = Intervals[i] 
            if ans[1]>=curr[0]:
                ans[1] = max(ans[1],curr[1])

            else:
                res.append(ans)
                ans = curr
        res.append(ans)
        return res
#drivercode
obj = Solution()
Intervals=[[6,8],[1,9],[2,4],[4,7]]

print(obj.overlappedInterval(Intervals))