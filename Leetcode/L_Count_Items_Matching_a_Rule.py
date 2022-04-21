# Count Items Matching a Rule
class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        counter = 0
        for i in range(0, len(items)):
            if(ruleKey == "type"):
                if(items[i][0] == ruleValue):
                    counter = counter + 1
                else:
                    pass
            elif(ruleKey == "color"):
                if(items[i][1] == ruleValue):
                    counter = counter + 1
                else:
                    pass
            elif(ruleKey == "name"):
                if(items[i][2] == ruleValue):
                    counter = counter + 1
                else:
                    pass
            else:
                pass

        return counter


X = Solution()
print(X.countMatches([["phone", "blue", "pixel"], [
      "computer", "silver", "phone"], ["phone", "gold", "iphone"]], "type", "phone"))
