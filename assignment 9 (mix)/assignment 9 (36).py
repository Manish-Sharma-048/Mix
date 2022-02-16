'''
Write a Python program to solve (x + y) * (x + y)
'''

num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

def prob(x,y):
   z = (x + y) * (x + y)
   return z

print(prob(num1,num2))
