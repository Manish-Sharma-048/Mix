'''
Write a Python program to display your details like name, age, address in three different lines.
'''

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
if age<0:
   raise ValueError("Age should be a positive number")
add = input("Please enter your address: ")

print("Name:",name,"\nAge:",age,"\nAddress:",add)
