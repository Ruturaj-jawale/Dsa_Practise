class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # if n <= 0:
        #     return False
        # while n % 3 == 0:
        #     n //= 3
        # return n == 1
        max_int = 2**31 - 1
        k = int(math.log(max_int, 3))
        largestP = 3 ** k
        return n > 0 and largestP % n == 0