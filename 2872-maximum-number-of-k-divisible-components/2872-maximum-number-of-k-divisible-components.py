class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict
        g = defaultdict(list)

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        self.count = 0

        def dfs(node, parent):
            total = values[node]
            for nei in g[node]:
                if nei == parent:
                    continue
                sub = dfs(nei, node)
                total += sub

            if total % k == 0:
                self.count += 1
                return 0

            return total

        dfs(0, -1)
        return self.count
        