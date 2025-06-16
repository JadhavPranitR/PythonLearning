'''Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''
try:
    # Step 1: Write user input to a file named output.txt
    user_input = input("Enter some text to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(user_input + '\n')

    # Step 2: Append additional data to the same file
    additional_data = input("Enter additional text to append to the file: ")
    with open('output.txt', 'a') as file:
        file.write(additional_data + '\n')

    # Step 3: Read and display the final content of the file
    with open('output.txt', 'r') as file:
        print("\nFinal content of output.txt:")
        for line in file:
            print(line.strip())
except Exception as e:
    print("Error:", e)
