class Solution(object):
    from collections import defaultdict
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
       


        n = len(grid)
        diagonals = defaultdict(list)

        # Step 1: Collect diagonals
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])

        # Step 2: Sort each diagonal
        for key, vals in diagonals.items():
            if key >= 0:  # bottom-left (including main)
                vals.sort(reverse=True)  # non-increasing
            else:  # top-right
                vals.sort()  # non-decreasing

        # Step 3: Refill grid
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)

        return grid
