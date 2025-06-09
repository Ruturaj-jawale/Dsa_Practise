class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet_Sum = nums[0]+ nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i +1, len(nums) -1


            while left < right:
                current_Sum = nums[i] + nums[left] + nums[right]

                if abs(current_Sum - target) < abs(closet_Sum - target):
                    closet_Sum = current_Sum

                if current_Sum < target:
                    left += 1
                elif current_Sum > target:
                    right -= 1
                else:
                    return current_Sum 
        return closet_Sum
        