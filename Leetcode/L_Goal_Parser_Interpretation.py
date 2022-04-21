# Goal Parser Interpretation
class Solution:
    def interpret(self, command):
        return command.replace("()", "o").replace("(al)", "al")


X = Solution()
print(X.interpret("G()()()()(al)"))
