from typing import List
from functools import lru_cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # 4 diagonal directions
        dirs = [(1,1), (-1,-1), (1,-1), (-1,1)]  # ↘ ↖ ↙ ↗
        turn = {0:2, 2:1, 1:3, 3:0}  # clockwise mapping

        # sequence pattern: 1 → 2 → 0 → 2 → 0 → ...
        def expected(k: int) -> int:
            if k == 0: return 1
            return 2 if k % 2 == 1 else 0

        @lru_cache(None)
        def dfs(i: int, j: int, d: int, turned: int, seqIndex: int) -> int:
            # out of bounds
            if not (0 <= i < n and 0 <= j < m):
                return 0
            # value mismatch
            if grid[i][j] != expected(seqIndex):
                return 0

            best = 1  # count current cell

            # continue in same direction
            di, dj = dirs[d]
            ni, nj = i + di, j + dj
            best = max(best, 1 + dfs(ni, nj, d, turned, seqIndex+1))

            # try clockwise turn (if not already turned)
            if not turned:
                nd = turn[d]
                di, dj = dirs[nd]
                ni, nj = i + di, j + dj
                best = max(best, 1 + dfs(ni, nj, nd, 1, seqIndex+1))

            return best

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  # must start with 1
                    for d in range(4):  # try all 4 diagonals
                        ans = max(ans, dfs(i, j, d, 0, 0))
        return ans
