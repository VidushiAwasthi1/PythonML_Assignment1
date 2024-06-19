#Write a python program that takes a list of numbers and returns their sum. 
n=int(input("Enter length of list: "))
l=[]
for i in range(n):
    element=int(input("Enter a number: "))
    l.append(element)
sum=0
for i in l:
    sum+=i
print("The sum of numbers is",sum)
