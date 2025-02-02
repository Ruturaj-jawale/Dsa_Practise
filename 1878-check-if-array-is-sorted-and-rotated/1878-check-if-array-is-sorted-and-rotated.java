class Solution {
    public boolean check(int[] nums) {
        int n = nums.length;

        int[] chechSorted = new int[n];

        for(int rotationOffset = 0; rotationOffset < n; ++rotationOffset){
            int currIndex = 0;
            for(int index = rotationOffset; index < n; ++index){
                chechSorted[currIndex++] = nums[index];
            }
            for(int index = 0; index < rotationOffset ; ++index){
                chechSorted[currIndex++] = nums[index];
            }

            boolean isSorted = true;
            for(int index = 0 ; index < n - 1; ++index){
                if(chechSorted[index] > chechSorted[index + 1]){
                    isSorted = false;
                    break;
                }
            }

            if(isSorted){
                return true;
            }
        }

        return false;
        
    }
}