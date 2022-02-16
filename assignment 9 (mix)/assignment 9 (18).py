'''
Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
'''

string = input("Enter string: ")
string1 = string.lower()

li = list(string1.split(" "))

if li[0] == 'is':
    print(string)
else:
    print("Is " + string)
