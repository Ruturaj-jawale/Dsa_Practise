class Solution {
    public boolean isPowerOfFour(int n) {
        if(n <= 0){
            return false;

        }

        int max_i = (int) Math.pow(2,31) -1;
        int k = (int) (Math.log(max_i)/ Math.log(4));
        long LargestP =(long) Math.pow(4, k);

        return (LargestP % n == 0) && (Math.log(n)/ Math.log(4) % 1 == 0);
        }}