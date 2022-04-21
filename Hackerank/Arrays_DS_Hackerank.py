# So this is a solution of the problem Arrays - DS of Hackerank


Y = int(input())
X = list(map(int, input().split(" ")))
X.reverse()

# print(X)
for i in range(0, len(X)):
    print(X[i], end=" ")
