class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefix = [0] * (n + 1)
        positions = [fruits[i][0] for i in range(n)]

        for i in range(n):
            prefix[i + 1] = prefix[i] + fruits[i][1]

        def get_sum(l, r):
            return prefix[r+1] - prefix[l] 

        max_f = 0
        left = 0

        for right in range(n):
            while left <= right:
                l_pos = fruits[left][0]
                r_pos = fruits[right][0]

                dist = min(abs(startPos - l_pos)+ (r_pos - l_pos) ,  abs(startPos - r_pos) + (r_pos - l_pos) )

                if dist <= k:
                    max_f = max(max_f, get_sum(left, right))
                    break
                left += 1
            
        return max_f

