# Author :- Bishal Kunwar 290, Date: 26th sept 2023

'''# In this task, you need to perform interactive tests to answer some questions related to Python programming. Each question is worth one mark.

a) Using the + operator on different/mixed types:

You need to test what happens when you use the + operator on different/mixed types, such as string + list, list + tuple, etc. Record your observations.

b) Using + operator with a dictionary:

You need to test whether the + operator works when one of the operands is a dictionary. Record your observations.

c) Testing the append method and keys method:

You need to test whether the append method works for both lists and strings, and whether you can use the keys method on lists. Provide your observations, and consider what append assumes about its subject object.

d) Determining the type of object returned by slicing or concatenating lists or strings:

You need to determine the type of object you get back when you slice or concatenate two lists or two strings. Record your observations.'''

# Solution:
# A solution using the + operator on different/mixed types:

# String + List: If we use +Operator on a String and a List, we will face TypeError because these data types are not compatible for direct addition however using the typecasting use can do perform addition besides our test case scenario.
def str_list():
    str1 = "Bishal"
    list1 = [1,2,3]

    result = str1+list1
    print(result)

str_list()

# Error: TypeError: can only concatenate str (not "list") to str


# String + Tuple: If we use +Operator on a String and a tuple, we will face TypeError because these data types are not compatible for direct addition however using the typecasting use can do perform addition besides our test case scenario.
def str_tuple():
    str1 = "Bishal"
    tuple1 = (1,2,3)

    result = str1+tuple1
    print(result)

str_tuple()

# Error: TypeError: can only concatenate str (not "tuple") to str


# List + Tuple : If we use +  operator with the list and tuples , if we typecast tuple to list then it will concatinate and return the new list with result items from both as a new list.
def list_tuple():
    list1 = [1,2,3]
    tuple1 = (1,2,3)

    result = (list1+tuple1) 
    print(result) # Error TypeError: can only concatenate list (not "tuple") to list

    result1 = list1 + list(tuple1)
    print(result1) # the result will be : [1, 2, 3, 1, 2, 3]

list_tuple()


# String + Integer : TTo use + operator to concatenate a string and an integer, we should first convert the integer to a string.
def string_integer():
    str1 = "Bishal"
    num1 = 487

    result = str1+num1
    print(result)

string_integer()

# Error: TypeError: can only concatenate str (not "int") to str

# Conclusion :- To perform + operation in different data types in python, the operands must be compatible for the operations that we intend to carry out, for that we can use explict type conversions using the built in functions like: str(), int(), float(), list(), tuple() and so on.

