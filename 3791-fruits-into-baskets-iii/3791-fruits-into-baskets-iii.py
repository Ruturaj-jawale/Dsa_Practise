# class Solution:
#     def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
#         n = len(fruits)

#         sorted_bask = sorted((cap, i) for i , cap in enumerate(baskets))

#         available = SortedList(i for i in range(n))

#         used = [False] * n
#         unplaced = 0

#         for f in fruits:
#             idx = bisect_left(sorted_bask,(f, -1))

#             found = False
#             while idx < n:
#                 cap, original_index, = sorted_bask[idx]
#                 if not used[original_index]:

#                     used[original_index] = True
#                     found = True
#                     break

#                 idx += 1

#             if not found:
#                 unplaced += 1
#         return unplaced


# from bisect import bisect_left
# from typing import List

# class Solution:
#     def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
#         n = len(fruits)
#         used = [False] * n
#         unplaced = 0

#         for fruit in fruits:
#             placed = False
#             for i in range(n):
#                 if not used[i] and baskets[i] >= fruit:
#                     used[i] = True
#                     placed = True
#                     break
#             if not placed:
#                 unplaced += 1
#         return unplaced
      


from bisect import bisect_left
from sortedcontainers import SortedList
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        
        # Step 1: Prepare and sort baskets by capacity
        indexed_baskets = sorted([(cap, i) for i, cap in enumerate(baskets)])
        
        # Step 2: Maintain a SortedList of original basket indices
        unused_indices = SortedList(range(n))
        
        used = [False] * n
        unplaced = 0

        for fruit in fruits:
            # Binary search: first basket with capacity >= fruit
            idx = bisect_left(indexed_baskets, (fruit, -1))
            found = False
            
            while idx < n:
                cap, original_index = indexed_baskets[idx]
                if not used[original_index]:
                    used[original_index] = True
                    found = True
                    break
                idx += 1
            
            if not found:
                unplaced += 1

        return unplaced
