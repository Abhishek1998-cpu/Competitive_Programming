# Final Value of Variable After Performing Operations
# Array String

class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        counter = 0
        for i in range(0, len(operations)):
            if(operations[i] == "X++" or operations[i] == "++X"):
                counter += 1
            if(operations[i] == "X--" or operations[i] == "--X"):
                counter -= 1
        return counter


X = Solution()
print(X.finalValueAfterOperations(["--X", "X++", "X++"]))
print(X.finalValueAfterOperations(["++X", "++X", "X++"]))
print(X.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))
