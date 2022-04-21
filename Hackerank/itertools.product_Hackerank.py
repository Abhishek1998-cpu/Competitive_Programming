# So this is the solution of the problem itertools.product() from Hackerank
from itertools import product  # To use itertools product we have to import this file


def cartesian(arr1, arr2):
    Y = list(product(arr1, arr2))
    return Y


X = list(map(int, input().split(" ")))
Z = list(map(int, input().split(" ")))
result = cartesian(X, Z)
result2 = tuple(result)
print(*result2, sep=" ")

# Given below are different ways of how we can multiply two arrays and get it's cartesian product with the help of itertools product

# 1st Method
# Y = list(product([1, 2], [3, 4]))
# print(Y)

# 2nd Method
# A = [[1, 2, 3], [3, 4, 5]]
# B = list(product(*A))
# print(B)

# 3rd Method
# B = [[1, 2, 3], [3, 4, 5], [7, 8]]
# A = list(product(*B))
# print(A)
