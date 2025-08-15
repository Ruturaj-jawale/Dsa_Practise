class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max_i = 2**31 - 1
        k = int(math.log(max_i, 4))
        largestP = 4 ** k
        return n > 0 and (largestP % n == 0) and math.log(n, 4).is_integer()