class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brok = set(brokenLetters)
        word = text.split(" ")
        count = 0

        for w in word:
            if not any(c in brok for c in w):
                count +=1


        return count
