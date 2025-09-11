class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        
        # Extract vowels from s
        extracted = [ch for ch in s if ch in vowels]
        
        # Sort by ASCII
        extracted.sort()
        
        # Rebuild the string
        res = []
        idx = 0  # index for sorted vowels
        
        for ch in s:
            if ch in vowels:
                res.append(extracted[idx])
                idx += 1
            else:
                res.append(ch)
        
        return "".join(res)
