class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)

        filtered = [nums[0]]
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                filtered.append(nums[i])

        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1
        return count
        