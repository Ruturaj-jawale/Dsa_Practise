class Solution {
    public int countHillValley(int[] nums) {
        List<Integer> filter = new ArrayList<>();

        filter.add(nums[0]);
        for(int i = 1; i < nums.length ; i++){
                if(nums[i] != nums[i-1]){
                    filter.add(nums[i]);
                }
        }
        int count = 0;
        for(int i = 1; i < filter.size() - 1; i++){
            int p = filter.get( i -1);
            int c = filter.get(i);
            int n = filter.get(i + 1);

            if(c > p && c > n){
                count += 1;
            }else if(c < p && c < n){
                count += 1;
            }
        }
        return count;
    }
}