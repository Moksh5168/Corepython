Year=int(input("Enter the year which you want to known leap year"))
if((Year%400==0) or  (Year%100!=0) and (Year%4==0)):
    print("Given yera is Leap year")
else:
    print("Given Year is not Leap Year") 