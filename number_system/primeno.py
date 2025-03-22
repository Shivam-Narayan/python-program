# Python3 program to display Prime numbers till N
#function to check if a given number is prime
def is_Prime(n):
  #since 0 and 1 is not prime return false.
    if(n==1 or n==0):  return False
  
  #Run a loop from 2 to n-1
    for i in range(2,n):
    #if the number is divisible by i, then n is not a prime number.
        if(n%i==0):
            return False
  
  #otherwise, n is prime number.
    return True

# Print all prime numbers between 1 and 100
print("Prime numbers between 1 and 100:")
for i in range(1, 101):
    if is_Prime(i):
        print(i, end=" ")
        
        
# #Another methods...
# from sympy import primerange

# # Print all prime numbers between 1 and 100 using SymPy
# print("Prime numbers between 1 and 100:")
# print(list(primerange(1, 101)))