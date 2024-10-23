# Python program password generator

import random

#letters (Lowercase and Uppercase)
lower = "abcdefghijklmnopqrstuvwxyz" # lowercase
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # uppercase

#numbers and symbols
numbers = "0123456789"
symbols = "@#%*S_-"

all = lower + upper + numbers + symbols # combines all above
length = 10 # Set digit length (e.g 10)

password = "".join(random.sample(all,length)) #random all above

#Print Generated 10 digit password
print("Generated Password: ", password)