# Rectangle Overlap
# Maths

class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        # Defining Co-ordinates
        x11 = rec1[0]
        y11 = rec1[1]
        x21 = rec1[2]
        y21 = rec1[3]
        x12 = rec2[0]
        y12 = rec2[1]
        x22 = rec2[2]
        y22 = rec2[3]

        if (x22 <= x11 or y22 <= y11 or y12 >= y21 or x12 >= x21) or (x11 == x21 or y11 == y21 or x12 == x22 or y12 == y22):
            return False
        else:
            return True
