#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
op=input("Enter operator(+,-, *, /): ")
if op=='+':
    print("Sum of numbers is",num1+num2)
elif op=='-':
    print("Difference of numbers is",num1-num2)
elif op=='*':
    print("Multipication of numbers is",num1*num2)
elif op=='/':
    print("Division of numbers is",num1/num2)
else:
    print("Invalid input")
