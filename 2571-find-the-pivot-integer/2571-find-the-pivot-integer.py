class Solution:
    def pivotInteger(self, n: int) -> int:
        T = n * ( n + 1) // 2
        x = isqrt(T)

        return x if x * x == T else -1
        