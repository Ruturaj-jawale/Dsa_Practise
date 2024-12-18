class Solution {
    public int[] finalPrices(int[] prices) {
        int k = prices.length;
        int[]res = new int[k];

        for(int i = 0 ; i<k;i++ ){
            res[i]=prices[i];

        

        for(int j =i+1;j<k;j++){
            if(prices[j]<=prices[i]){
                res[i] -= prices[j];
                break;
            }
        }

    //     for (int j = i + 1; j < k; j++) {
    // if (prices[j] <= prices[i]) {
    //     res[i] -= prices[j];
    //     break;
    
        }
        return res;
    }
}