class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        m, n = len(mat), len(mat[0])
        
        # Step 1: build width matrix
        width = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    width[i][j] = width[i][j-1] + 1 if j > 0 else 1
        
        # Step 2: count submatrices
        ans = 0
        for i in range(m):
            for j in range(n):
                if width[i][j] > 0:
                    min_width = width[i][j]
                    for k in range(i, -1, -1):
                        min_width = min(min_width, width[k][j])
                        if min_width == 0: break
                        ans += min_width
        return ans
