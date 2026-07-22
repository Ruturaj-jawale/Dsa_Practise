class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def backtrack(start, curre, remaining):
            if remaining == 0:
                ans.append(curre[:])
                return
            if remaining < 0:
                return 
        
            for i in range (start, len(candidates)):
                curre.append(candidates[i])

                backtrack(i, curre, remaining - candidates[i])

                curre.pop()

        backtrack(0, [], target)
        return ans 

        