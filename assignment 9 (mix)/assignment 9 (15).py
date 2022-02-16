'''
Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. 
'''

num = int(input("Enter number: "))

if num >= 17:
    print("The absolute difference which is multiplied by 2 is: ",(num - 17)*2)
else:
    print("The difference between the given number and 17 is: ",17 - num)
