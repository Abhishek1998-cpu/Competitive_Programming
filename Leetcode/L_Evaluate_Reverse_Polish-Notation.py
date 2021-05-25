# Evaluate Reverse Polish Notation
# Stack
class Solution:
    def evalRPN(self, tokens) -> int:
        def eval(b, a, op):
            if op == "+":
                return a + b
            elif op == "-":
                return a-b
            elif op == "*":
                return a * b
            else:
                return int(a / b)

        st = []
        for t in tokens:
            if t in "+-*/":
                st.append(eval(st.pop(), st.pop(), t))
            else:
                st.append(int(t))
        return st.pop()


X = Solution()
print(X.evalRPN(["2", "1", "+", "3", "*"]))
