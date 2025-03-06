n = int(input())
x = n 
sum = 0
while x>0:
    dig = x % 10
    sum += dig ** 3
    x = x // 10
if sum == n:
    print("yes")
else:
    print("no")
