# Find Duplicate File in System


import collections
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths):
        content_hash = collections.defaultdict(list)
        for path in paths:
            s = path.split(" ", 1)
            directory = s[0]
            rest = s[1]
            for f in rest.split(" "):
                name, content = f.split("(")
                content = content.rstrip(")")
                content_hash[content].append(directory + "/" + name)
        results = []
        for key in content_hash.keys():
            if len(content_hash[key]) > 1:
                results.append(content_hash[key])
        return results


X = Solution()
print(X.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)",
                       "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
