import random
import math


def binary_search(l):
    length = len(l1)
    print("Number of elements:", length)
    while True:
        if i == l[math.ceil(length/2)-1]:
            return True
        elif i < l[math.ceil(length/2)-1]:
            l = l[:math.ceil(length/2)-1]
        else:
            l = l[math.ceil(length/2):]
        if length == 1:
            return False
        length = len(l)


if __name__ == '__main__':
    l1 = random.sample(range(1000),random.randint(1,10))
    print("l=",l1)
    l1.sort()
    print("l=", l1)
    print("Enter a number:")
    i = int(input())
    if binary_search(l1):
        print(i, "is in the list. I used Binary Search")
    else:
        print(i, "is not in the list.I used Binary Search")