
# Count Primes
# Prime Number = Only Divides by 1 and Itself

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        primes = [True for i in range(n + 1)]
        count = 0
        p = 2
        while p*p <= n:
            if primes[p]:
                for i in range(p * 2, n + 1, p):
                    primes[i] = False
            p += 1
        primes[0], primes[1] = False, False
        for p in range(n):
            if primes[p]:
                count += 1
        return count


X = Solution()
print(X.countPrimes(10))
