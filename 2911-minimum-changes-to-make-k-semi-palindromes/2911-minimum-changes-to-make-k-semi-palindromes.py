class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        n = len(s)

        cost = [[0] * n for _ in range(n)]

        for l in range(n):
            for r in range(l + 1,n):

                length = r - l + 1  
                best = float('inf')

                for d in range(1, length):

                    if length % d != 0:
                        continue

                    changes = 0

                    for offset in range(d):

                        left = l + offset 
                        right = ( 
                            l + offset
                            +((length - 1 - offset) // d) * d
                        )   

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d
                    best = min(best, changes) 
                cost[l][r]  = best 
        
        INF = float('inf')

        dp = [[INF] * (n + 1) for _ in range(k+1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):
                for p in range(2 *(parts - 1), i - 1):

                    dp[parts][i] = min(
                        dp[parts][i],
                        dp[parts - 1][p] + cost[p][i - 1]
                    )
        
        return dp[k][n]