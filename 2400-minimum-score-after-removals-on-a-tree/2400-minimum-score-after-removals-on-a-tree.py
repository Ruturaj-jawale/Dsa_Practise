from typing import List
from collections import defaultdict

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        tree = defaultdict(list)
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        parent = [-1] * n
        subtree_xor = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        time = [0]
        edge_list = []

        def dfs(u, par):
            parent[u] = par
            in_time[u] = time[0]
            time[0] += 1

            xor_val = nums[u]
            for v in tree[u]:
                if v != par:
                    edge_list.append((v, u))  # child, parent
                    xor_val ^= dfs(v, u)
            subtree_xor[u] = xor_val

            out_time[u] = time[0]
            time[0] += 1
            return xor_val

        total_xor = dfs(0, -1)

        def is_ancestor(u, v):
            # Check if u is ancestor of v
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]

        min_score = float('inf')

        for i in range(len(edge_list)):
            for j in range(i + 1, len(edge_list)):
                a, _ = edge_list[i]
                b, _ = edge_list[j]

                if is_ancestor(a, b):
                    comp1 = subtree_xor[b]
                    comp2 = subtree_xor[a] ^ subtree_xor[b]
                    comp3 = total_xor ^ subtree_xor[a]
                elif is_ancestor(b, a):
                    comp1 = subtree_xor[a]
                    comp2 = subtree_xor[b] ^ subtree_xor[a]
                    comp3 = total_xor ^ subtree_xor[b]
                else:
                    comp1 = subtree_xor[a]
                    comp2 = subtree_xor[b]
                    comp3 = total_xor ^ comp1 ^ comp2

                max_x = max(comp1, comp2, comp3)
                min_x = min(comp1, comp2, comp3)
                min_score = min(min_score, max_x - min_x)

        return min_score
