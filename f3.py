#Write a python program that calculates the factorial of a given number. 

num=int(input("Enter a number: "))
factorial=1

for i in range(2,num+1):
    factorial*=i
    
print(factorial)
