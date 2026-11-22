"""
write a function called find_max that takes three numbers as parameters
 and print the largest one. 
"""
#3 numbers are different
def find_max(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(n1)
    elif n2>n1 and n2>n3:
        print(n2)
    else:
        print(n3)

find_max(1,10,3)                