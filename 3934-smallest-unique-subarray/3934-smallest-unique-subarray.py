from collections import Counter
from typing import List


class Solution:

  def smallestUniqueSubarray(self, nums: List[int]) -> int:
    n = len(nums)

    # Double hashing parameters to avoid collisions
    MOD1, BASE1 = 10**9 + 7, 1315423911
    MOD2, BASE2 = 10**9 + 9, 2654435761

    # Precompute powers
    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)
    for i in range(n):
      pow1[i + 1] = (pow1[i] * BASE1) % MOD1
      pow2[i + 1] = (pow2[i] * BASE2) % MOD2

    # Precompute prefix hashes
    pref1 = [0] * (n + 1)
    pref2 = [0] * (n + 1)
    for i in range(n):
      pref1[i + 1] = (pref1[i] * BASE1 + nums[i]) % MOD1
      pref2[i + 1] = (pref2[i] * BASE2 + nums[i]) % MOD2

    def has_unique_subarray(length: int) -> bool:
      counts = Counter()
      p1, p2 = pow1[length], pow2[length]
      for i in range(n - length + 1):
        h1 = (pref1[i + length] - pref1[i] * p1) % MOD1
        h2 = (pref2[i + length] - pref2[i] * p2) % MOD2
        counts[(h1, h2)] += 1
      return any(c == 1 for c in counts.values())

    left, right = 1, n
    ans = n
    while left <= right:
      mid = (left + right) // 2
      if has_unique_subarray(mid):
        ans = mid
        right = mid - 1
      else:
        left = mid + 1

    return ans
