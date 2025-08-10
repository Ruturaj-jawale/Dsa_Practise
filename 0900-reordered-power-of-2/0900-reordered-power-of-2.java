class Solution {
    public boolean reorderedPowerOf2(int n) {
        String target = sortDigits(n);

        Set<String> powerSet = new HashSet<>();
        for(int i = 0; i < 31; i++){
            int pow = 1 << i;
            powerSet.add(sortDigits(pow));
        }

        return powerSet.contains(target);
        
    }

    private String sortDigits(int num){
        char[] arr = String.valueOf(num).toCharArray();
        Arrays.sort(arr);
        return new String(arr);
    }
}