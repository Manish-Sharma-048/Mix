'''
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
'''

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

def num(num1,num2):
   if num1 == num2 or (num1+num2) == 5 or (num1-num2) == 5 or (num2-num1) == 5:
      return True
   else:
      return False

print(num(num1,num2))
