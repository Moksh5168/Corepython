data=["naman","eve","madam","radar","raju"]
new_list=[]
count=0
for i in data:
    if i == i[::-1]:
        new_list.append(i)
print("Palindrome list is: ",new_list)
    

        
