#Write a python program that removes all punctuation from a given string. 
import string
str1=input("Enter a string: ")
for char in string.punctuation:
    str1 = str1.replace(char, "")
print(str1)
