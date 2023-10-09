L = [1, 2, 4, 8, 16, 32, 64]
X = 5
# improve performance to move the 2 ** X expression outside the loops
value_to_find = 2 ** X
if value_to_find in L:
    print('found at index', L.index(value_to_find))
else:
    print(X, 'not found')
