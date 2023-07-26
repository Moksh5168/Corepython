no=int(input("Enter a number"))

#45678
count=0

#45678!=0  true
#4567!=0  true
#456!=0  true
#45!=0 true
#4!=0  true
#0!=0 false

while no!=0:
    #1
    #2 3 4 5

    count+=1
    #45678///10=4567
    #4567//10=456
    #456//10=45
    #45//10=4
    #4//10=0

    no=no//10
print(count)













num=int(input("enter the num"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"factorial of {num} is {factorial}")