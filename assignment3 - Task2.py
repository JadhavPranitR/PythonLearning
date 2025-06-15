'''
Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''
# import math  #Code with the math module to perform calculations
# # Solution
# value = float(input("Enter a number: "))
# sqrt_value = math.sqrt(value)
# log_value = math.log(value)
# sin_value = math.sin(value)

# print("Square root:", sqrt_value)
# print("Natural logarithm:", log_value)
# print("Sine (radians):", sin_value)

from math import *
# Code without the math module to perform calculations
# Solution  
value = float(input("Enter a number: "))
sqrt_value = sqrt(value)    
log_value = log(value)
sin_value = sin(value)
print("Square root:", sqrt_value)
print("Natural logarithm:", log_value)
print("Sine (radians):", sin_value)
