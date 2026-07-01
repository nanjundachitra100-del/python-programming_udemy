n=int(input("Enter a year:"))

if(n%4==0):
    if(n%100):
        if(n%400==0):
            print("the year is leap year")
        else:
            print("not a leap year")
    else:
        print("it is a leap year")
else:
    print("it is not a leap year")