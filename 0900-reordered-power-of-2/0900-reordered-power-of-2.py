class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def sort_value(x):
            return ''.join(sorted(str(x)))

        power_set = {sort_value(1 << i) for i in range(31)}

        return sort_value(n) in power_set


        