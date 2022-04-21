# This is a solution of the problem "Intro_to_set" from Hackerank


def average(array):
    # your code goes here
    SetY = set(array)
    len_of_array = len(SetY)
    listY = list(SetY)
    Sum_of_listY = sum(listY)
    Avg = float(Sum_of_listY/len_of_array)
    return Avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# Note: Conversion of List to set and vice versa is used here

# Here is an example of the Note
# Y = set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# print(Y)
