class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        def powmod(x, y):
            result = 1
            x %= mod
            for _ in range(y):
                result = (result * x) % mod
            return result
         
        ans = 1
        for digit in b:
            ans = powmod(ans, 10) * powmod(a, digit) % mod
        return ans