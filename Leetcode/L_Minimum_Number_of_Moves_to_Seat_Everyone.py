# Minimum Number of Moves to Seat Everyone
# Array Sorting

class Solution:
    def minMovesToSeat(self, seats, students) -> int:
        seats.sort()
        students.sort()
        Total = 0
        for x, y in zip(seats, students):
            Difference = abs(x-y)
            Total = Total + Difference
        return Total


X = Solution()
print(X.minMovesToSeat([3, 1, 5], [2, 7, 4]))
print(X.minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]))
print(X.minMovesToSeat([2, 2, 6, 6], [1, 3, 2, 6]))
