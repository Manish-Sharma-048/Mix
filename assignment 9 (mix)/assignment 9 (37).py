'''
Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
'''

p_a = int(input("Please enter the Principle Amount: "))
r_o_i = float(input("Please enter the Rate of Interest: "))
tenure = int(input("Please enter the Tenure: "))

if tenure<1:
   raise ValueError("Tenure should be atleast one year")

def fut_val(x,y,z):
   f_v = x*y/100*z
   return f_v

print("The future value you need to pay is: ",fut_val(p_a,r_o_i,tenure))
