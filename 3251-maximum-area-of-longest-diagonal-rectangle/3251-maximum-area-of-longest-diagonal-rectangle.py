class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = -1
        max_area = -1

        for l, w in dimensions:
            diag_sq = l * l + w * w
            area = l * w
            if diag_sq > max_diag or (diag_sq == max_diag and area > max_area):
                max_diag = diag_sq
                max_area = area
        

        return max_area


        