arr = [11,434,500,2,2,2,500,6,7]
#print(set(arr))
unique =[]
for num in arr:
    if num not in unique:
        unique.append(num)
print(unique)