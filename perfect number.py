n = int(input("Enter a number: "))
sum = 0

for i in range(1, n): 
    if n % i == 0:
        sum += i

if n == sum:
    print("It is a perfect number")
else:
    print("It is NOT a perfect number")
