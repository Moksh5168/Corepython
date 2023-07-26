num1=int(input("Enter the first no"))
num2=int(input("Enter the second no"))
num3=int(input("Enter the third no"))
if(num1>num2):
    print("num 1 is greater than num2")
    if(num1>num3):
        print("num1 is greater than num3")
    else:
        print("num3 is greater than num1")
else:
     print("num 2 is greater than num1")