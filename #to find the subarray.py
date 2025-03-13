#to find the subarray
'''arr = [1,23,5]
sub_array = []
for i in range(len(arr)):
    for j in range(i,len(arr)):
        sub_array.append(arr[i:j+1])
print(sub_array)
t.c=0(n)^2'''


# best use kadanes algorithm for max sum 
# it is best for both +ve/-ve elements
#t.c is O(n)

'''arr = [-1,3,-4,5,6]
n = len(arr)
max_sum = float('-inf')
current_sum = 0

for i in arr:
    current_sum += i 
    max_sum = max(max_sum , current_sum)
    if current_sum < 0:
        current_sum = 0
print(max_sum)'''

#prefix sum for arrays k
nums = [1, 2, 3, -3, 1, 2, 3]
target = 3
count  = 0
prefix_sum = 0
seen = {0:1}

for i in nums:
    prefix_sum += i 
    
    if prefix_sum - target in seen:
        count += seen[prefix_sum - target]
    seen[prefix_sum] = seen.get(prefix_sum , 0) + 1
print(count)
    

