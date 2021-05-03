# Course Schedule 3


import heapq


class Solution:
    def scheduleCourse(self, courses) -> int:
        courses.sort(key=lambda x: x[1])
        heap = []
        max_time = 0
        for time, end_time in courses:
            heapq.heappush(heap, -time)
            max_time += time
            if max_time > end_time:
                big_time = heapq.heappop(heap)
                max_time += big_time

        return len(heap)


X = Solution()
print(X.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
