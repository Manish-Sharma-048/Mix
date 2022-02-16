'''
Write a Python program to add two objects if both objects are an integer type.
'''

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

def add(num1,num2):
   if not (isinstance(num1,int) and isinstance(num2,int)):
      raise TypeError("Number should be integer")
   else:
      return num1+num2

print(add(num1,num2))
