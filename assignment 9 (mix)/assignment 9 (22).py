'''
Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
'''

string = input("Enter string: ")
string = string.strip()

num = int(input("Enter number: "))

if len(string) > 2:
    str1 = string[:2]
    print(str1 * num)
else:
    print(string * num)
