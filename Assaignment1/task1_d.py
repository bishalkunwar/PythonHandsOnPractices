# Author :- Bishal Kunwar 290, Date: 26th sept 2023

'''d) Determining the type of object returned by slicing or concatenating lists or strings:
You need to determine the type of object you get back when you slice or concatenate two lists or two strings. Record your observations.'''

# Slicing lists: When we slice a list, we will get a new list containing the selected elements.
list1 = [1,2,3,4,5]
list1_sliced = list1[1:3]

print(list1_sliced) 
# Result : [2, 3] , while slicing list, it will give result from length.0 to length.all -1. if [1:3] then it will return items from index 1 and 2.


# Concatenating lists: When we concatenate two lists using the + operator, we will get a new list containing all elements from both lists
list1 = [1,2,3]
list2 = [3,4,5]

list_concat = list1+list2
print(list_concat)

# Result :- [1, 2, 3, 3, 4, 5]


# Slicing String: When we slice a string, we will get a new string containing the selected characters.
string = "bishal kunwar"
sliced_str = string[2:4]

print(sliced_str) # Result: "sh"



# Concatenating strings:
# When we concatenate two strings using the + operator, we get a new string containing both strings joined together
string1 = "Bishal"
string2 = "suzan"

concat_str = string1+string2
print(concat_str) #Result : Bishalsuzan