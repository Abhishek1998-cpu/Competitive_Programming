class Solution:
    def shuffle(self, nums, n):
        # # print(n+10)
        # lenn = len(nums)
        # X = nums[0:n]
        # Y = nums[n:lenn]
        # Z = []
        # # print(X)
        # # print(Y)
        # for i in range(0, lenn):
        #     for i in range(0, len(X)):
        #         Z.append(X[i])
        #         break
        #     for i in range(0, len(Y)):
        #         Z.append(Y[i])
        #         break
        # return Z
        ans = []
        N = len(nums)
        for i in range(N//2):
            ans.append(nums[i])
            ans.append(nums[i-N//2])
        return ans


X = Solution()
Arr = [10, 10, 20, 304]
print(X.shuffle(Arr, 2))
