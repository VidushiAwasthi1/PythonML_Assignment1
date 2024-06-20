#Write a program that reads data from a CSV file and prints it to the console. 
import csv

file_path = 'your_file.csv'

try:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
