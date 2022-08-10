def maximumSubarraySum(arr):
    n = len(arr)
    maxSum = -1e8

    for i in range(0, n):
        currSum = 0
        for j in range(i, n):
            currSum = currSum + arr[j]
            if(currSum > maxSum):
                maxSum = currSum

    return maxSum

if __name__ == "__main__":
    # Your code goes here
    a = [1, 3, 8, -2, 6, -8, 5];
    b = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maximumSubarraySum(a));
    print(maximumSubarraySum(b))