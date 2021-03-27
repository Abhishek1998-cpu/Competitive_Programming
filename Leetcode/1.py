# class Solution:
#     def maximum69Number(self, num):
#         Arr = []
#         num = list(str(num))
#         for j in range(0, len(num)):
#             for i in range(0, len(num)):
#                 if (num[i] == "9"):
#                     num[i] = "6"
#                     break
#                 else:
#                     num[i] = "9"
#                     break
#         Arr.append("".join(num))

#         return Arr

class Solution:
    def maximum69Number(self, num):
        return int(str(num).replace("6", "9", 1))


X = Solution()
print(X.maximum69Number(9996))
print(X.maximum69Number(9669))
