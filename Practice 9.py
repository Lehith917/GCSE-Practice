#Generate password 8 characters long 3 digits 3 characters 2 special cahracters
import random
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
nums="1234567890"
specs="!£$%?@#"
a=random.choice(chars)
b=random.choice(chars)
c=random.choice(chars)
d=random.choice(nums)
e=random.choice(nums)
f=random.choice(nums)
g=random.choice(specs)
h=random.choice(specs)
p=[a,b,c,d,e,f,g,h]
random.shuffle(p)
password=""
for x in p:
    password=password+x
print("Your password is:"+password)

