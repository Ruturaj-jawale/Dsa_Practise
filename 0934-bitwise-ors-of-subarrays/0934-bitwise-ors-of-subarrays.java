class Solution {
    public int subarrayBitwiseORs(int[] arr) {
        Set<Integer> ans = new HashSet();
        Set<Integer> list1 = new HashSet();

        list1.add(0);

        for(int x : arr){
            Set<Integer> list2 = new HashSet();
            for (int y : list1)
               list2.add(x | y);
            list2.add(x);
            list1 = list2;
            ans.addAll(list1);
        }

        return ans.size();

     }
}