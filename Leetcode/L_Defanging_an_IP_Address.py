# Defanging an IP Address
class Solution:
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")


X = Solution()
print(X.defangIPaddr("255.100.50.0"))
