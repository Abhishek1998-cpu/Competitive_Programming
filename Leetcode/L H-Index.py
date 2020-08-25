# H Index --> at least h >= h 
# H Index of 5 means there are at least 5 paper which are cited 5 times or more. 

class Solution:
    def hIndex(self, list):
        citations.sort()
        n, i = len(citations), 1
        while i <= n:
            if citations[n-i] < i: break
            i += 1
        return i-1

citations = list(map(int, input().split(" "))) 
X = Solution()
print(X.hIndex(citations))

# This is the solution of the problem H-index of the leetcode