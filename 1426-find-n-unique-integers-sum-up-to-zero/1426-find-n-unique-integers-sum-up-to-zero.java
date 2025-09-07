class Solution {
    public int[] sumZero(int n) {
            // int[] res  = new int[n];
            // int index = 0;

            // for (int i = 1; i <= n/2 ; i++){
            //     res[index++] = i;
            //     res[index++] = -i;

            // }

            // if (n % 2 == 1){
            //     res[index] = 0;
            // }

            // return res;


            List<Integer> resl = new ArrayList<>();
            for(int i = 1; i <= n/2; i++){
                resl.add(i);
                resl.add(-i);
            }

            if(n % 2 == 1){
                resl.add(0);
            }

            int[] res = new int[resl.size()];
            for(int i = 0; i < resl.size(); i++){
                res[i] = resl.get(i);
            }


            return res;
    }
}