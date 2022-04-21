# Number of Students doing Homework at a Given time

class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        ans = 0
        m = zip(startTime, endTime)
        for s, e in m:
            if s <= queryTime <= e:
                ans += 1
        return ans


X = Solution()
print(X.busyStudent([1, 2, 3], [3, 2, 7], 4))
