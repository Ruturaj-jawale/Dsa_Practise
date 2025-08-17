class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        p = [0.0] * (n + 1)

        for x in range(k , n+ 1):
            p[x] = 1.0

        windows = sum(p[k:min(n , k + maxPts - 1) + 1])

        for x in range(k-1, -1 ,-1):
            p[x] = windows / maxPts
            windows += p[x]
            if x + maxPts <= n:
                windows -= p[x + maxPts]
        
        return p[0]
        