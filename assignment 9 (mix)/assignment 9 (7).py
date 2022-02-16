'''
Write a Python program to accept a filename from the user and print the extension of that.
'''

f_name = input("Enter filename: ")
f_ex = f_name.split(".")

print("The extension of the file is : " + repr(f_ex[-1]))
