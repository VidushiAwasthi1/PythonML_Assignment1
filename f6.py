#Write a program that reads the content of a text file and prints it to the console.
file_path = 'sample.txt'

with open(file_path, 'r') as file:
    
    file_content = file.read()
    
    print("File Content:\n", file_content)
