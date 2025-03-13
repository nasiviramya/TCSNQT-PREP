arr = [1,5,6,7,8]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[i] < arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)

