n = int(input())
arr = list(map(int ,input().split(',')))
arr = [x+4 for x in arr]
print(arr)