#LCM and hcf of 2 number
n1=int(input("enter the no1:"))
n2=int(input("enter the no2:"))

#to find lcm
for i in range(max(n1,n2),1+(n1*n2)):
    if i%n1==i%n2==0:
        lcm=i
print("lcm of",n1,"and",n2,"is",lcm)