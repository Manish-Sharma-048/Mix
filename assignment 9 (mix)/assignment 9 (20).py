'''
Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
'''

num = int(input("Enter the number: "))

if num%2 == 0:
    print("The entered number:",num,"is an even number.")
else:
    print("The entered number:",num,"is an odd number.")
