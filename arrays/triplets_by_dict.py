def find_triplet(arr,n,tar):
    map = {}
    res = []
    for i in range(n-1):
        s = arr[i]
        if s not in map:
            
            map[s] = [i]
    
    for j in range(n-1):
        for k in range(i+1,n):
            rs = tar-arr[j]-arr[k]
            if rs in map:
                check = map[rs]
                if check[0]!=j and check[0]!=k:
                    res.append((arr[check[0]],arr[j],arr[k]))

    return res





A = [1,4,45,6,10,8]
n=len(A)
print(find_triplet(A,n,22))