L = []
X = 6  # The number of powers of 2 you want
# Use a for loop and the list append method to generate the powers-of-2 list (L) instead of hardcoding a list literal.
for i in range(X):
    L.append(2 ** i)
print(L)
