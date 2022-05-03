#Password Generator Project
import random

from numpy import append, insert
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
clave = []

for i in range(nr_letters):
    #clave.append(letters[random.randint(0,len(letters)-1)])  
    clave.append(random.choice(letters))
     
for i in range(nr_numbers):
    #clave.append(numbers[random.randint(0,len(numbers)-1)])  
    clave.append(random.choice(numbers))
     
for i in range(nr_symbols):
    #clave.append(symbols[random.randint(0,len(symbols)-1)])   
    clave.append(random.choice(symbols))

# for i in range(len(clave)):
#     n =random.randint(0,len(clave)-1)
#     aux.append(clave[n])
#     clave.pop(n)

random.shuffle(clave)

result= "".join(clave)
  
print(f"Your password is: {result}")