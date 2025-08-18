class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s = 0
        e = len(letters) - 1

        while s <= e:
            mid = s +(e-s)//2

            if target < letters[mid] :
                e = mid - 1
            else :
                s = mid + 1

            

        return letters[s % len(letters)]
            

        