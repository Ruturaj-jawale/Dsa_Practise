class Solution {
    private boolean canPartition(String numStr, int target, int index, int currentSum) {
        if (index == numStr.length()) {
            return currentSum == target;
        }
        
        for (int j = index; j < numStr.length(); j++) {
            int part = Integer.parseInt(numStr.substring(index, j + 1));
            if (currentSum + part <= target && canPartition(numStr, target, j + 1, currentSum + part)) {
                return true;
            }
        }
        
        return false;
    }

    public int punishmentNumber(int n) {
        int total = 0;
        
        for (int i = 1; i <= n; i++) {
            int square = i * i;
            String squareStr = String.valueOf(square);
            
            if (canPartition(squareStr, i, 0, 0)) {
                total += square;
            }
        }
        
        return total;
    }

   
}
