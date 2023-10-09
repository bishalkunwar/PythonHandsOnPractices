L = [1, 2, 4, 8, 16, 32, 64]
X = 5
# Remove the loop completely by rewriting the example with a simple in operator membership expression
if 2 ** X in L: 
    print('found at index', L.index(2 ** X))
else:
    print(X, 'not found')
