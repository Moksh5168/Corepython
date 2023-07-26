s=input("Enter name you want to count ")
dict={}

for i in s:
    if s.count(i)==0:
        dict.update({i:0})
    elif s.count(i)==1:
        dict.update({i:1})
    elif s.count(i)==2:
        dict.update({i:2})
    elif s.count(i)==3:
        dict.update({i:3})
print(dict)
