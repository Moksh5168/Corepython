#Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type.

#take a list with numbers



list_a=[4,5,2,3,7,8,1,9,4,10]

new_list=set(list_a)
print(new_list)
first_max=max(new_list)
new_list.remove(first_max)
second_max=max(new_list)
new_list.remove(second_max)
third_max=max(new_list)
print(third_max)


