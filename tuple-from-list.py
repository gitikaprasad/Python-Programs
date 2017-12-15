import random
from operator import itemgetter


def getkey(l):
        return l[1]

l = random.sample(range(1000),12)
print("l=",l)
length=len(l)
print("length",length)
l2=[]

i=0
if length%3==1:
    l.append(random.randint(1,1000))
while i<length:
     a=(l[i],l[i+1],l[i+2])
     l2.append(a)
     i+=3
print("l2=",l2)
l2=sorted(l2,key= itemgetter(1))
print("l2=",l2)

m= lambda c : max(c)
print(m(l))