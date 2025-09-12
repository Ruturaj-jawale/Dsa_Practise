class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vs = set("aeiou")
        v = sum( 1 for ch in s if ch in vs)

        return v > 0
        # if v == 0:
        #     return False
        # if v % 2 == 1:
        #     return True
        # return False
        