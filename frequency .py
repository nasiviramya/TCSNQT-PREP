arr = [1,5,6,7,9,0,0,3,3,1]
d={}
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d) #"counted the frequency of elements"
sort = sorted(d.values())
print(sort) #"sorted the values
print(max(sort)) # found the maximum element