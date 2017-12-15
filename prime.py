print("enter a number:")
prime = True
n = int(input())
if n == 1 or n == 2:
    prime = True
else:
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            prime = False
            break

if not prime:
    print(n,"is not a prime number")
else:
    print(n, "is a prime number")