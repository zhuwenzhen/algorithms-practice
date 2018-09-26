"""
1324. Count Primes
Count the number of prime numbers less than a non-negative number, n.
"""
import math
from itertools import count, islice

class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def isPrime(self, n):
        if n < 2: return False

        for i in islice(count(2), int(math.sqrt(n) - 1)):
            if n % i == 0: return False
        return True

    def countPrimes(self, n):
        if n < 3:
            return 0
        count = 0
        for i in range(n):
            if self.isPrime(i):
                count += 1
        return count

    def countPrimes(self, n):
        # write your code here
        if n < 3:
            return (0)

        prime = [True] * n

        prime[0] = prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                prime[i * i: n: i] = [False] * len(prime[i * i: n: i])
        return (sum(prime))

s = Solution()
print(s.countPrimes(6))
# for i in range(100):
#     print("for number ", i)
#     s.isPrime(i)