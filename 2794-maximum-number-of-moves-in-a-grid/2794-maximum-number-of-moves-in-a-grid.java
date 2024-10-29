class Solution {
    public int maxMoves(int[][] grid) {
        int maxRow = grid.length - 1;
        int maxCol = grid[0].length - 1;
        int res = 0;
        
        // Create a memoization table initialized to -1 (indicating uncomputed results)
        int[][] memo = new int[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                memo[i][j] = -1;
            }
        }
        
        // Start from each cell in the first column
        for (int i = 0; i <= maxRow; i++) {
            int tempRes = recursion(grid, i, 0, maxRow, maxCol, memo);
            res = Math.max(res, tempRes);
        }
        return res;
    }
    
    int recursion(int[][] grid, int row, int col, int maxRow, int maxCol, int[][] memo) {
        // Base case: Out of bounds check
        if (row < 0 || col > maxCol || row > maxRow) return 0;
        
        // If the result is already computed, return it from memo
        if (memo[row][col] != -1) return memo[row][col];
        
        int diagonalUp = 0, right = 0, diagonalDown = 0;
        
        // Move diagonally up
        if (row - 1 >= 0 && col + 1 <= maxCol && grid[row - 1][col + 1] > grid[row][col]) {
            diagonalUp = 1 + recursion(grid, row - 1, col + 1, maxRow, maxCol, memo);
        }
        
        // Move right
        if (col + 1 <= maxCol && grid[row][col + 1] > grid[row][col]) {
            right = 1 + recursion(grid, row, col + 1, maxRow, maxCol, memo);
        }
        
        // Move diagonally down
        if (row + 1 <= maxRow && col + 1 <= maxCol && grid[row + 1][col + 1] > grid[row][col]) {
            diagonalDown = 1 + recursion(grid, row + 1, col + 1, maxRow, maxCol, memo);
        }
        
        // Store the result in memo and return the maximum moves
        memo[row][col] = Math.max(diagonalUp, Math.max(right, diagonalDown));
        return memo[row][col];
    }
}
