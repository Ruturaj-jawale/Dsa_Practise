class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24 ) < 1e-6

            
            # recursive step

            for i in range(len(nums)):   #First Number
                for j in range(len(nums)):  #Second number

                    if i != j:
                        next_num = []   #list of remaining no

                        for k in range(len(nums)):
                            if k != i and k != j:
                                next_num.append(nums[k])

                        
                    
                        for op in ops(nums[i], nums[j]):
                            if dfs(next_num + [op]):
                                return True

            return False
        
        def ops(a, b):
            results = [a + b, a - b, b - a, a * b]

            if abs(b ) > 1e-6:
                results.append(a/b)
            if abs(a) > 1e-6:
                results.append(b/a)
            
            return results
        
        return dfs([float(x) for x in cards])
                            


        