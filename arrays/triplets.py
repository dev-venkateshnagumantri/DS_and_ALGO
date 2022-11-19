def find_triplet(arr,k):
    arr.sort()
    n = len(arr)
    res = []
    for i in range(n-2):
        l = i+1
        r = n-1
        while l<r:
            if arr[i]+arr[l]+arr[r]==k:
                res.append([arr[i],arr[l],arr[r]])
                l+=1
                r-=1
            elif arr[i]+arr[l]+arr[r]<k:
                l+=1
            else:
                r-=1
    return res

A = [1,4,45,6,10,8]
print(find_triplet(A,22))

'''O(n^2)'''