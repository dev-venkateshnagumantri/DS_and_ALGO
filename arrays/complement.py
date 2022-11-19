def solve(arr1,arr2):
    d = {}
    res = []
    for item in arr2:
        if item not in d.keys():
            d[item] = 1
        else:
            d[item]+=1
    for item in arr1:
        if item not in d.keys():
            res.append(item)
    return res
arr1 = [1,2,4,5,10]
arr2 = [2,1,0,5]
res = solve(arr1,arr2)

for i in res:
    print(i,end=" and ")
print(" are present in first but not in second array")