class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        
        powers = [1]
        while powers[-1] * 4 <= 10**9:
            powers.append(powers[-1] * 4)
        
        def prefix_Sum(n):
            if n <= 0:
                return 0
            total = 0
            prev = 1
            steps = 1

            for p in powers:
                end = min(n, 4 * p -1)
                if prev <= end:
                    total += (end - prev + 1) *steps

                if n <= 4 * p - 1:
                    break

                prev = 4 * p
                steps += 1

            return total

        ans = 0
        for l, r in queries:
            total_steps =  prefix_Sum(r) - prefix_Sum(l- 1)
            ans += (total_steps + 1) // 2

        return ans  