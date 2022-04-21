# Furthest Building You Can Reach
import heapq


class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        INF = 1 << 60
        heights = [INF] + heights
        N = len(heights)
        h = []
        for index in range(1, N):
            if heights[index] <= heights[index - 1]:
                continue
            delta = heights[index] - heights[index - 1]
            heapq.heappush(h, delta)

            while len(h) > ladders:
                bricks -= h[0]
                heapq.heappop(h)
            if bricks < 0:
                return index - 2
        return N - 2


X = Solution()
# print(X.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))
print(X.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))
