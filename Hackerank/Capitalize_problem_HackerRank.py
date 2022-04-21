# This is a Solution of the Capitalize! problem of Python HacerRank

s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)
