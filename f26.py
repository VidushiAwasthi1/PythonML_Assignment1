#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
str1=input("Enter a string: ")
fix=input("Enter suffix or prefix: ")
lfix=len(fix)
if str1[:lfix]==fix:
    print("The given string is the prefix")
elif str1[-lfix:]==fix:
    print("The given string is the suffix")
else:
    print("The given stirng is nither the prefix or the suffix")
