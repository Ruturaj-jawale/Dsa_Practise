class Solution {
    public int maximumLength(int[] nums, int k) {
       int n = nums.length;
       int[][] dp = new int[n][k];

       int maxLength = 1;

       for(int i = 0;i < n; i++){
        Arrays.fill(dp[i], 1);

       }

       for(int i = 1; i < n; i++){
        for(int j = 0; j < i; j++){
            int mod = (nums[i] + nums[j]) % k;

            dp[i][mod] = Math.max(dp[i][mod], dp[j][mod] + 1);
            maxLength = Math.max(maxLength, dp[i][mod]);

        }
       } 

       return maxLength;
    }
}