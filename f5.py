# Write a program that takes a string input from the user and writes it to a text file.
user_input = input("Enter a string: ")

with open("output.txt", "w") as file:
    file.write(user_input)

print("String written to 'output.txt'.")
