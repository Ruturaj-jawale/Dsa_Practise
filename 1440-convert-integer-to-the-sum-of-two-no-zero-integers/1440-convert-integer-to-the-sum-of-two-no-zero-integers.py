class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1,n):
            b = n - a
            if self.is_no_zero(a) and self.is_no_zero(b):
                return [a,b]

    def is_no_zero(self, num: int) -> bool:
        return '0' not in str(num)        