'''
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
'''

string = input("Enter string: ")
num = int(input("Enter the number: "))

if (num>0):
    print(string*num)
else:
    print('Invalid entry')
