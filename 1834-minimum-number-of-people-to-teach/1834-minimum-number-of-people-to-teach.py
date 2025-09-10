class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)

        lang_sets = [set(l) for l in languages]

        prob_user = set()
        for u, v in friendships:
            u -= 1
            v -= 1

            if lang_sets[u].intersection(lang_sets[v]):
                continue
            
            prob_user.add(u)
            prob_user.add(v)

        res = float('inf')

        for L in range(1, n + 1):
            cnt = 0
            for user in prob_user:
                if L not in lang_sets[user]:
                    cnt += 1
            res = min(res, cnt)
        return res

