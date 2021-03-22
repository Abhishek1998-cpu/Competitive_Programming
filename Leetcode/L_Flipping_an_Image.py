# Flipping an Image

# class Solution:
#     def flipAndInvertImage(self, image):
#         for i in image:
#             i.reverse()
#             for j in range(len(image)):
#                 i[j] ^= 1
#         return A

class Solution:
    def flipAndInvertImage(self, image):
        for i in image:
            i.reverse()
            for j in range(len(image)):
                i[j] ^= 1
        return image


X = Solution()
print(X.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
