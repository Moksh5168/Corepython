l1=()
n=int(input("enter the number of element you want to add into tuple:      "))
list2=list(l1)
for i in range(n):
    a=input("enter the elemnets :    ")
    list2.append(a)

l1=tuple(list2)    
print(l1)
