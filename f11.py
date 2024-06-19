#Write a python program that generates the first n numbers in the Fibonacci sequence.
n1=0
n2=1

x=int(input("Enter a number: "))
count = 0

while count < x:
    print(n1, end=" ")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
