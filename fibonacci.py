print("How many fibonacci number u want?: ")
n = int(input())
fib=[]
a=1
for i in range(0,n):
    if i <=1:
        fib.append(a)
    else:
        fib.append(fib[i-2]+fib[i-1])
print("Fibonacci number list: ",fib)