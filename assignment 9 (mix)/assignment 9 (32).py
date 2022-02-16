'''
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
'''

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

tot = num1 + num2


if tot>=15 and tot<=20:
   print("As the sum of",num1,"and",num2, "is in between 15 to 20, the output will be 20")
        
else:
   print(num1 + num2)
