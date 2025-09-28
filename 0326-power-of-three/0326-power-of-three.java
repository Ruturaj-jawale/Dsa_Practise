class Solution {
    public boolean isPowerOfThree(int n) {
        if(n <=  0 ){
            return false;
        }
            int num = (int) Math.pow(2,31)-1;
            int k = (int) (Math.log(num)/ Math.log(3));
            long P = (long) Math.pow(3, k);
            return (P % n == 0);
                }
}