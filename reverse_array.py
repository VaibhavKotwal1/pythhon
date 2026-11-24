#reverse the array
n=int(input("enter number of elements:"))
arr = list(map(int,input("enter elements:").split()))

results = arr[::-1]

print(results)