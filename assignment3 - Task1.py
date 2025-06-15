'''Task 1: Calculate Factorial Using a Function 


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.'''

# Solution
value = int(input("Enter a number to calculate its factorial: ")) 
def factorial(n):
    if n < 2:  # Base case for recursion
        # Factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n-1) # Recursive case
        # Multiply n by the factorial of (n-1)

# Sample usage
print(factorial(value))