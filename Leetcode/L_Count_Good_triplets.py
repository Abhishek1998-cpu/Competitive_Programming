# Count Good Triplets
class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        N = len(arr)
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count


X = Solution()
print(X.countGoodTriplets([3, 0, 1, 1, 9, 7],  7,  2,  3))
