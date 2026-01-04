n=[1,2,3,4,5,6,7,8,9,10]
even= filter(lambda x: x % 2 == 0, n)
odd= filter(lambda x: x % 2 != 0, n)
print("Even number are: ",list(even))
print("Odd number are: ",list(odd))