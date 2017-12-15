print("Enter a list of numbers, click enter to end")
l1=[]
i=input()
while i != '':
    i = int(i)
    l1.append(i)
    print("l1=", l1)
    i = input()
l2=[]
for i in l1:
    if i%2 == 0:
        l2.append(i)

print("Your list: ",l1)
print("Even elements: ",l2)