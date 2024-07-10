#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
myletters =""
mynumbers = ""
mysymbols = ""
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for char in range(1, nr_letters+1):
  myletters+= random.choice(letters)
print(myletters)
for char in range(1, nr_numbers+1):
  mynumbers+= random.choice(numbers)
print(mynumbers)
for char in range(1, nr_symbols+1):
  mysymbols+= random.choice(symbols)
print(mysymbols)
password = myletters + mynumbers + mysymbols
#print(password)
final_password=''.join(random.sample(password,len(password)))
print(f"Your final password is: {final_password}")
#new_password = str(password)
#print(new_password)

#password = str(letter)+str(symbol)+str(number)
#print(password)
  
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P