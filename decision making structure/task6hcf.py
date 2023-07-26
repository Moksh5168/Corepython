num1=int(input("Enter a number 1:->"))
num2=int(input("Enter a number 1:->"))
lcm=0
if num1>num2:
    max=num1
    min=num2
elif num2>num1:
    max=num2
    min=num1

hcf=0
for i in range(1,min+1):
    if(num1%i==0 and num2%i==0):
        hcf=i
print(hcf)