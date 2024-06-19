#Write a python program that checks if two strings are anagrams of each other. 
str1=input("Enter a string: ")
str2=input("enter another string: ")
l1=list(str1).sort()
l2=list(str2).sort()

if l1==l2:
    print("The strings are anagrams of each other.")
else:
    print("The strings are NOT anagrams of each other.")
