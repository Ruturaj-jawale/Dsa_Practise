from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        # Calculate total value of each item type
        weight = [1] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    weight[i] += 1

        # Sort item indices by descending price
        order = sorted(range(n), key=lambda i: -items[i][1])

        dp = [0] * (budget + 1)
        selected = [-10**9] * (budget + 1)

        ans = 0
        index = 0

        while index < n:

            price = items[order[index]][1]

            # Process items with the same price
            while index < n and items[order[index]][1] == price:

                i = order[index]
                w = weight[i]

                for c in range(budget, price - 1, -1):

                    selected[c] = max(
                        selected[c],
                        dp[c - price] + w
                    )

                    dp[c] = max(
                        dp[c],
                        dp[c - price] + w
                    )

                index += 1

            # Calculate answer for this minimum price
            for c in range(budget + 1):
                if selected[c] >= 0:
                    extra = (budget - c) // price
                    ans = max(ans, selected[c] + extra)

        return ans