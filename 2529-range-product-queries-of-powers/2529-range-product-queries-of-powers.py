class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        MOD = 10**9 + 7

        powers = []
        bit = 1
        while n :
            if n & 1:
                powers.append(bit)

            bit <<= 1
            n >>= 1

        powers.sort()

        prefix = [powers[0] % MOD]
        for i in range(1, len(powers)):
            prefix.append((prefix[-1] * powers[i]) % MOD)

        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                inv = pow(prefix[l - 1], MOD - 2, MOD)
                ans.append((prefix[r] * inv ) % MOD)
        return ans

        