import random
def play():
    global cow, bull
    cow, bull = (0, 0)
    for i in n1:
        if i in n2:
            if n1.index(i) == n2.index(i):
                cow += 1
            else:
                bull += 1



i=0
guess=0
n1=[]
ch='y'

while i<4:
    n = str(random.randint(0,9))
    if n not in n1:
        n1.append(n)
        i+=1
print("Number is : ",''.join(n1))
while ch!='n':
    print("Enter a 4 digit number:")
    n2=input()
    if len(n2)==4:
        guess+=1
        play()
        if (cow == 4 and bull == 0):
            print("you got it!!",guess," guesses")
            break
    else:
        print("Number must be 4 digit")
    print("you got", cow,"cows and ",bull,"bulls")
    print("Want to try again (Y/N)? ")
    ch=input()
