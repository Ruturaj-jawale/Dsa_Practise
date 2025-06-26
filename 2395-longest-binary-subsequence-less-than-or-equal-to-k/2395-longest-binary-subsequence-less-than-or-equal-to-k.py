class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        count = 0  # length of valid subsequence
        value = 0
        power = 0

        # # Include all '0's (they don't increase value)
        zeros = s.count('0')
        count = zeros

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            if power >= 31 :
                break
            if s[i] == '1':
                # Compute value if we add this 1 at current bit position
                if value + (1 << power) <= k:
                    value += (1 << power)
                    count += 1
            
            power += 1


        return count
