
class Solution {
    public long minCost(int[] basket1, int[] basket2) {
        Map<Integer, Integer> freq = new HashMap<>();
        int n = basket1.length;

        for(int num : basket1) freq.put(num, freq.getOrDefault(num, 0) + 1);
        for(int num : basket2) freq.put(num, freq.getOrDefault(num, 0) - 1);

        List<Integer> surplus = new ArrayList<>();
        int minElement = Integer.MAX_VALUE;

        for(Map.Entry<Integer, Integer> entry: freq.entrySet()){
            int value = entry.getValue();
            int fruit = entry.getKey();
            minElement = Math.min(minElement, fruit);

            if(value % 2 != 0) return -1;

            for(int i = 0; i< Math.abs(value) / 2; i++){
                surplus.add(fruit);
            }
        } 
        Collections.sort(surplus);
        long cost = 0;
        int m = surplus.size();

        for(int i = 0 ; i <m /2; i++){
            cost += Math.min(surplus.get(i), 2 * minElement);

        }

        return cost;
    }
}