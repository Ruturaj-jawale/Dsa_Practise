class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False]*n
        unplaced = 0

        for fruit in fruits:
            placed = False
            for j in range(n):
                if not used[j] and baskets[j] >= fruit:
                    used[j]  = True
                    placed = True
                    break 
            if not placed:
                unplaced += 1

        return unplaced