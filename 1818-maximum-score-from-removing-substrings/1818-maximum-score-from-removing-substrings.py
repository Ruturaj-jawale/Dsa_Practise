class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pattern(s, first, second, score):
            stack = []
            total = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(ch)
            return ''.join(stack), total

        total = 0
        if x > y:
            s, gain1 = remove_pattern(s, 'a', 'b', x)
            _, gain2 = remove_pattern(s, 'b', 'a', y)
        else:
            s, gain1 = remove_pattern(s, 'b', 'a', y)
            _, gain2 = remove_pattern(s, 'a', 'b', x)

        total = gain1 + gain2
        return total
