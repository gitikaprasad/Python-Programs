import random
l = ['rock','paper','scissor']
print("Enter your name: ")
name = input()
print("Hi",name,",let's play rock,paper and scissor.")
c='y'
while c == 'y':
    print("What you choose?")
    ch1 = input()
    i=random.randint(0,2)
    print("i=",i)
    ch2=l[i]
    print("ch1=",ch1)
    print("ch2=",ch2)
    if (ch1 == "rock" and ch2 == "scissor")or(ch1 == "scissor" and ch2=="paper") or (ch1 == "paper" and ch2 == "rock"):
        print("Congrats, you won.")
    elif ch1 == ch2:
        print("it's a tie")
    else:
        print("Sorry you lose")
    print("Want to play again (Y/N)")
    c=input()

