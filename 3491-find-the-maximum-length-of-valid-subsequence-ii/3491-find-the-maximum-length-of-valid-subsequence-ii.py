class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums);
        dp = [[1] * k for _ in range(n)]

        max_length = 1

        for i in range(1, n):
            for j in range(i):
                mod = (nums[i] + nums[j]) % k
                dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1)
                max_length = max(max_length, dp[i][mod])

        return max_length
        