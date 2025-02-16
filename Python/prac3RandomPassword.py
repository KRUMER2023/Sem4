# generate random password of a given length

import random
import string

length=int(input("Enter the length:"))
values=string.digits+string.punctuation+string.ascii_letters
password=""

for i in range(1,length+1):
    password+=random.choice(values)


print("Generated Password:", password)
