class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_int = 2**31-1
        k = int(math.log(max_int, 3))
        largest_p = 3 ** k
        return n > 0  and  (largest_p % n == 0) 