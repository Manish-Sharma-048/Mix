'''
Write a Python program to concatenate all elements in a list into a string and return it.
'''

li = ['Hi', 'how', 'are', 'you']

def conc(li):
    string = " ".join(li)
    return(string)

print(conc(li))
