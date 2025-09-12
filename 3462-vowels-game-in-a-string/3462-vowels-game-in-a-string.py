class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # vs = set("aeiou")
        # v = sum( 1 for ch in s if ch in vs)

        # return v > 0
        return  sum( 1 for ch in s if ch in set("aeiou")) > 0
        