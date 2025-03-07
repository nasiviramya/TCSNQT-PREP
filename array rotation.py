arr = [1,2,3,4,5]
k = 7
k = k % len(arr)
arr[:] = arr[-k:]+arr[:-k]
print(arr)  #TC:O(n)