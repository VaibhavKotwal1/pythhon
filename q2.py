#write a functions that print all the factors of a number entered by users 

def print_factors():
     num=int(input("Enter a number = "))
     for i in range(1,num+1):
          if num %i==0:
               print(i,end="  ")

print_factors ()               