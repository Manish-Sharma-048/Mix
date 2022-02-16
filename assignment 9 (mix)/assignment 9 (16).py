'''
Write a Python program to test whether a number is within 100 of 1000 or 2000.
'''

num = int(input("Enter number between (0-2000): "))

if (num <= 99):
    print("The number is between 0 and 100")
elif (num > 99 and num <= 1000):
    print("The number is between 100 and 1000")
else:
    print("The number is between 1000 and 2000")
