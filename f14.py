#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines. 

str2=""
str1=input("Enter a multiline string: ")
while str1!="":
    str2=str2+'\n'+str1
    str1=input()
print(str2)
