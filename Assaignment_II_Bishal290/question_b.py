L = [1, 2, 4, 8, 16, 32, 64]
X = 5
for i, value in enumerate(L): #use a for loop with an else clause, to eliminate the explicit list-indexing logic
    if 2 ** X == value:
        print('at index', i)
        break
else:
    print(X, 'not found')
