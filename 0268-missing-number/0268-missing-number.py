class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        

        sum_n = (n * (n+1)) // 2
        

        arr_sum = sum(nums)
        

        return sum_n - arr_sum    
        