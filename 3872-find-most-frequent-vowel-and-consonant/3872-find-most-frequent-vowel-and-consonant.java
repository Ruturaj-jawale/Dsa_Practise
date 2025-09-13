class Solution {
    public int maxFreqSum(String s) {
        Set<Character > vowels = new HashSet<>(Arrays.asList('a','e','i','o','u'));
        Map<Character, Integer> freq  = new HashMap<>();
        for (char ch : s.toCharArray()){
            freq.put(ch, freq.getOrDefault(ch,0)+1);
        }
        int maxV = 0;
        int maxC = 0;
        for(Map.Entry<Character, Integer> entry : freq.entrySet()){
            char ch = entry.getKey();
            int count = entry.getValue();

            if(vowels.contains(ch)){
                maxV = Math.max(maxV, count);
            }else{
                maxC  = Math.max(maxC, count);

            }

        }

        return maxV + maxC;
    }
}