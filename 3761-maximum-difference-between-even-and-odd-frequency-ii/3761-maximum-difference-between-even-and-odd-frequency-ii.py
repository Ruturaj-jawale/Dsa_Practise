class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def get_status(cnt_a, cnt_b):
            return ((cnt_a & 1) << 1) | (cnt_b & 1)

        n = len(s)
        ans = float('-inf')

        for a in range(5):  # Characters '0' to '4'
            for b in range(5):
                if a == b:
                    continue

                best = [float('inf')] * 4
                cnt_a = cnt_b = 0
                prev_a = prev_b = 0
                left = -1

                for right in range(n):
                    ch = ord(s[right]) - ord('0')
                    if ch == a:
                        cnt_a += 1
                    if ch == b:
                        cnt_b += 1

                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = get_status(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)

                        left += 1
                        ch_left = ord(s[left]) - ord('0')
                        if ch_left == a:
                            prev_a += 1
                        if ch_left == b:
                            prev_b += 1

                    right_status = get_status(cnt_a, cnt_b)
                    opposite_status = right_status ^ 0b10

                    if best[opposite_status] != float('inf'):
                        ans = max(ans, cnt_a - cnt_b - best[opposite_status])

        return -1 if ans == float('-inf') else ans
