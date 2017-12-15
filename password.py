import random
import string
s1 = string.ascii_letters
s2 =  string.digits
s3 = string.punctuation
s = s1+s2+s3
len = 0
print("Letters: ",s)
print("Enter password length(Must be greater than or equal to 8) : ")
try:
    len = int(input())
except (ValueError, TypeError):
    len = -1
if len >= 8:
    pwd = random.sample(s1,len-5)+ random.sample(s2,3) + random.sample(s3,2)
    print("Password: ",pwd)
    pwd = ''.join(pwd)
    print("Password: ",pwd)
elif len == -1:
    print("length must be an integer")
else:
    print("Password length can't be less than 8 :(")