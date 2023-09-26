# Author :- Bishal Kunwar 290, Date: 26th sept 2023

# Append methods for lists: In lists, appe d method add the item to the last index of the original list.
def list_appending():
    list1 = [1,2,3]
    list1.append(4)

    print(list1)
    # Result: [1, 2, 3, 4]
list_appending()


# Append method for string: As Strings are immutable, so append method do not works for string().
def str_append():
    str1 = "bishal"
    str1.append("suzan")

    print(str1) # Error: AttributeError: 'str' object has no attribute 'append'

str_append()


# Keys methods on lists: The keys() method is used to retrieve the keys from a dictionary, and it does not work on lists.
list1 = [1,2,3]
keys = list.keys()

#Error: AttributeError: type object 'list' has no attribute 'keys'

 