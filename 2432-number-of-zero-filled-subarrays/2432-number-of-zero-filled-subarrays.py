class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        conZ = 0

        for num in nums:
            if num == 0:
                conZ += 1
                count += conZ
            else:
                conZ = 0
        return count
        