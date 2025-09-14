class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        word_set = set(wordlist)

        lower_map = {}
        for w in wordlist:
            lw = w.lower()
            if lw not in lower_map:
                lower_map[lw] = w
        

        def devowel(word):
            vowels = "aeiou"
            return "".join("*" if c in vowels else c for c in word)

        vowel_map = {}
        for w in wordlist:
            vw = devowel(w.lower())
            if vw not in vowel_map:
                vowel_map[vw] = w

        ans = []
        for q in queries:
            if q in word_set:
                ans.append(q)
            elif q.lower() in lower_map:
                ans.append(lower_map[q.lower()])
            elif devowel(q.lower()) in vowel_map:
                ans.append(vowel_map[devowel(q.lower())])
            else:
                ans.append('')

        return ans
        