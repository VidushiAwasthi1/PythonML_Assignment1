#Write a python program that counts the occurrences of a specific element in a list. 
count=0
n=int(input("Enter length of list: "))
l=[]
for i in range(n):
    element=input("Enter a character: ")
    l.append(element)
c=input("Enter the element whose occurance has to be counted: ")
for i in l:
    if i==c:
        count+=1
print(count)
