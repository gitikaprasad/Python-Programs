print("Enter a word:")
x=input()

l = list(x)
z=sorted(x)
print("z=",z)
y = list(reversed(l))

print("y=",y)
print("l=",l)
#l.reverse()
#print("l=",l)
if l == y:
    print("palindrome")
else :
    print("not palindrome")
