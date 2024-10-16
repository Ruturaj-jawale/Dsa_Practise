class Solution {
    public String longestDiverseString(int a, int b, int c) {
        return happyString(a , b , c , "a" , "b" , "c");
    }

    public String happyString(int a , int b , int c , String aStr , String bStr , String cStr)
    {
        if(a < b)
            return happyString(b , a , c , bStr , aStr , cStr);

        if(b < c)
            return happyString(a , c , b , aStr , cStr , bStr);

        if(b == 0)
            return aStr.repeat(Math.min(2 , a));

        int aUsed = Math.min(2 , a);
        int bUsed = a-aUsed >= b ? 1 : 0;

        return aStr.repeat(aUsed) + bStr.repeat(bUsed) + 
                happyString(a-aUsed , b-bUsed , c , aStr , bStr , cStr);
    }
}