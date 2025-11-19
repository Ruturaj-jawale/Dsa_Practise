class Solution {
    public int climbStairs(int n) {
        if(n <= 2 ) return n;
        int oneStepBefore = 2;
        int twoStepBefore = 1;
        int current = 0;

        for(int i = 3; i <= n; i++){
            current = oneStepBefore + twoStepBefore;
            twoStepBefore = oneStepBefore;
            oneStepBefore = current;

        }

        return current;
        
    }
}