class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left: int , right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            temp1 = expand_from_center(i, i)

            temp2 = expand_from_center(i, i + 1)

            if len(temp1) > len(longest):
                longest = temp1
            if len(temp2) > len(longest):
                longest = temp2
        return longest
        