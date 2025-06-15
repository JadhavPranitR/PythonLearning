#Task 2: Create a Personalized Greeting.
'''Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
4.  The greeting message should be in the format: "Hello, [Full Name]! Welcome to the Python program."
5.  Always keep the 1st letter of the first name and last name in capital letter.
'''
#Solution:
# Create a Personalized Greeting
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name.capitalize() + " " + last_name.capitalize()
print("Hello, " + full_name + "! Welcome to the Python program.")