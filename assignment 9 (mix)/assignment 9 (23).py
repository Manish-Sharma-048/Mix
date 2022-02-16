'''
Write a Python program to test whether a passed letter is a vowel or not.
'''

letter = input("Enter letter: ")
letter1 = letter.lower()
vow = ('a','e','i','o','u')

if letter1 in vow:
    print("Entered letter",letter,"is a vowel")
else:
    print("Entered letter",letter,"is not a vowel")
