# Jump Game 2
# Array
# Greedy
# BFS

class Solution:
    def jump(self, nums) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res


X = Solution()
print(X.jump([2, 3, 1, 1, 4]))
