#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input. 
temp=input("Enter the temperature: ")
if temp[-1]=='C':
    res=int(temp[:-2])*9/5 +32
    var='F'
elif temp[-1]=='F':
    res=(int(temp[:-2])-32)*5/9
    var='C'
else:
    print("invalid input")
print("Resulting temp is",res,var)

