#Write a python program that returns the minimum and maximum valuesin a list of numbers. 
n=int(input("Enter length of list: "))
l=[]
for i in range(n):
    element=int(input("Enter a number: "))
    l.append(element)
print("Maximum element of list is",max(l))
print("Minimum element of list is",min(l))
