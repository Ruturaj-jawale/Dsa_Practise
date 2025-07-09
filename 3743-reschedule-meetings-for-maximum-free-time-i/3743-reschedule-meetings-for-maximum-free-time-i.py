from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        max_gap = 0
        current_duration = 0

        for i in range(n):
            # Add duration of current meeting to sliding window
            current_duration += endTime[i] - startTime[i]

            # Calculate boundaries for the gap
            left_bound = 0 if i < k else endTime[i - k]
            right_bound = eventTime if i == n - 1 else startTime[i + 1]

            # Calculate potential free time in this gap
            available_gap = right_bound - left_bound - current_duration
            max_gap = max(max_gap, available_gap)

            # Slide the window: remove oldest meeting duration if needed
            if i >= k - 1:
                current_duration -= endTime[i - k + 1] - startTime[i - k + 1]

        return max_gap
