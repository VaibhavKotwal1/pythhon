"""
write a function that ask a number from user and prints if that 
 number is odd or even
"""
def odd_even():
    num=int(input("Enter a number = "))
    if num %2==0:
        print("number is even")
    else:
        print("number is odd ")    

odd_even()
