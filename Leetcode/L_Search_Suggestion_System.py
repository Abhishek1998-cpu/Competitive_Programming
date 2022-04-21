# Search Suggestion System
# String

class Solution:
    def suggestedProducts(self, products, searchWord: str):
        output = []
        products.sort()
        for i, c in enumerate(searchWord):
            tmp = []
            for p in products:
                if i < len(p) and c == p[i]:
                    tmp.append(p)
            output.append(tmp[: 3])
            products = tmp
        return output


X = Solution()
print(X.suggestedProducts(
    ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
