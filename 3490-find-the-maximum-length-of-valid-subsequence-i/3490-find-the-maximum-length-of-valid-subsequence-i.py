class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        even_only = sum(1 for num in nums if num % 2 == 0 )
        odd_only = sum(1 for num in nums if num %2 == 1)
        alt_even = self.get_alternating(nums, 0)
        alt_odd = self.get_alternating(nums, 1)

        return max(even_only, odd_only, alt_even, alt_odd)

    def get_alternating(self, nums, start_parity):
        ex = start_parity
        count = 0
        for num in nums:
            if num % 2 == ex:
                count += 1
                ex ^= 1
        return count