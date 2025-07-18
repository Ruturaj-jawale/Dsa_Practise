class Solution {
    public long minimumDifference(int[] nums) {
        int n = nums.length /3;

        long[] prefixSum = new long[nums.length];
        long[] suffixSum = new long[nums.length];

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        long prefixTotal = 0;
        for(int i = 0; i < 2 * n; i++){
            prefixTotal += nums[i];
            maxHeap.offer(nums[i]);
            if(maxHeap.size() > n){
                prefixTotal -= maxHeap.poll();
            }
            if(maxHeap.size() == n){
                prefixSum[i] = prefixTotal;
            }
        }

        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        long suffixTotal = 0;
        for(int i = nums.length- 1; i >= n; i--){
            suffixTotal += nums[i];
            minHeap.offer(nums[i]);
            if(minHeap.size() > n){
                suffixTotal -= minHeap.poll();
            }if(minHeap.size() == n){
                suffixSum[i] = suffixTotal;
            }
        }

        long result = Long.MAX_VALUE;
        for(int i = n - 1; i < 2 * n ; i++){
            result = Math.min(result, prefixSum[i] - suffixSum[i + 1]);
        }

     return result;    
    }
}