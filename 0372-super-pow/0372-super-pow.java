class Solution {
    private static final int mod = 1337;

    public int superPow(int a, int[] b) {
        int result = 1;
        for (int digits : b){
            result  = powMod(result , 10) * powMod(a, digits) % mod;

        }
        return result;
    }
    public int powMod(int x, int y){
        int res = 1;
        x %= mod;
        for(int  i = 0; i < y; i++){
            res = ( res * x) % mod;
        }
        return res;

    }
}