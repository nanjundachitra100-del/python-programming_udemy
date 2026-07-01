num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
operation=input("Enter the operation + ,- ,* ,/ ,%: ")

if(operation=='+'):
    print(num1+num2)
elif(operation=='-'):
    print(num1-num2)
elif(operation=='*'):
    print(num1*num2)
elif(operation=='/'):
    print(num1/num2)
elif(operation=='%'):
    print(num1%num2)
else:
    print("Invalid operation or number entered")