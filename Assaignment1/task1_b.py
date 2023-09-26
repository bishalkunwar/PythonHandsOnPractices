# Author :- Bishal Kunwar 290, Date: 26th sept 2023

'''Using + operator with a dictionary:

You need to test whether the + operator works when one of the operands is a dictionary. Record your observations.'''

# Solution: The + operator does not work for dictionary concatenation. To merge dictionaries, you should use dictionary unpacking ({**dict1, **dict2}) or the update() method.
def dict_dict():
    dict1 = {"id" : 1, "name" : "Bishal"}
    dict2= {"id" : 2, "name" : "Sujan"}
    
    # result = dict1+dict2
    # print(result) # Error: TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

    # dictionary unpacking
    result2 = {**dict1, **dict2}
    print(result2) # Result: {'id': 2, 'name': 'Sujan'}

    # update() method
    dict1.update(dict2)
    print(dict1) # Result: {'id': 2, 'name': 'Sujan'}

dict_dict()