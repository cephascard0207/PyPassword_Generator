#PyPassword_Generator
#Created By Cephas Cardozo
#Developed using Python

#imports
import random

#variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#printStatements & inputs
print("Welcome to the PyPassword Generator!")
print("Created by Cephas Cardozo\nDeveloped using Python\n\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#list
password_list = []

#for_loop
for char in range(1, nr_letters + 1):
  password_list += random.choice(letters)
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

#spacebar_print
print()

#random_shuffle_list
random.shuffle(password_list)
#variable
password = ""

#for_loop
for char in password_list:
  password += char


#final_f-string_print_statement
print(f"Your password is : {password}")