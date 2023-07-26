data=["naman","raju","anna","eve"]
count=0
for i in data:
    if i == i[::-1]:
        print("Palindrome Name in List:",i)
        count+=1
print("Total Palindrome name in list: ",count)

        