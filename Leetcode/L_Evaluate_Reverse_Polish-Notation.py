# Important Question of Stack
# Evaluate Reverse Polish Notation
# Stack
# Reverse Polish Notation = Postfix Notation

# Approach:
# Accessing all elements in the array, if the element is not matching with the special character (‘+’, ‘-‘,’*’, ‘/’) then push the element to the stack.

# Then whenever the special character is found then pop the first two-element from the stack and perform the action and then push the element (resultant element) to stack again.

# Repeat the above two process to all elements in the array

# At last pop the element from the stack and print the Result


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
