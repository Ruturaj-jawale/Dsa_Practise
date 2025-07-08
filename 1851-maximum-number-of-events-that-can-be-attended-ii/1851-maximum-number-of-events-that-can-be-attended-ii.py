from bisect import bisect_right
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by endDay
        events.sort(key=lambda x: x[1])
        
        # Extract end days for binary search
        end_days = [e[1] for e in events]
        n = len(events)
        
        # Precompute previous non-overlapping event index for each event
        prev = []
        for i in range(n):
            # Find the rightmost event that ends before current event starts
            idx = bisect_right(end_days, events[i][0] - 1) - 1
            prev.append(idx)
        
        # Initialize DP table: dp[i][j] = max value using first i events with j selections
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            start, end, val = events[i - 1]
            for j in range(1, k + 1):
                # Don't take this event
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                # Take this event
                if prev[i - 1] != -1:
                    dp[i][j] = max(dp[i][j], dp[prev[i - 1] + 1][j - 1] + val)
                else:
                    dp[i][j] = max(dp[i][j], val)

        return dp[n][k]
