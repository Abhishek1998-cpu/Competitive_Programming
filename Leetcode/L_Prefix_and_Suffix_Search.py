# Prefix and Suffix Search


from collections import defaultdict


class WordFilter:

    def __init__(self, words):
        self.p = defaultdict(set)
        self.s = defaultdict(set)
        seen = set()
        N = len(words)
        for i in range(N-1, -1, -1):
            if words[i] in seen:
                continue
            seen.add(words[i])
            W = words[i]
            K = len(W)
            for k in range(K+1):
                self.p[W[:k]].add(i)
                self.s[W[k:]].add(i)

    def f(self, prefix: str, suffix: str) -> int:
        i = self.p[prefix]
        j = self.s[suffix]
        overlap = i & j
        if not overlap:
            return -1
        return max(overlap)


# Your WordFilter object will be instantiated and called as such:
