'''
Write a Python program to check whether a specified value is contained in a group of values.  
Test Data : 
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

li = [1, 5, 8, 3]
num = int(input("Entered number: "))

if num in li:
    print(li,": True")
else:
    print(li,": False")
