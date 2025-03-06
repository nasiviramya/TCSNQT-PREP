n = int(input())
if n <=1:
    print("it is not prime number")
else:
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            print("it is not prime number")
            is_prime = False
            break
    if is_prime :
        print('it is prime number')