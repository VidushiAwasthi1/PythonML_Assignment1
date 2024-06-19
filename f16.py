#Write a program in python that counts the frequency of each character in a string.
input_string = input("Enter a string: ")
char_frequency = {}   
    
for char in input_string:
    
    char_frequency[char] = char_frequency.get(char, 0) + 1


for char, freq in char_frequency.items():
    print(char,':',freq)

user_input = input("Enter a string: ")
