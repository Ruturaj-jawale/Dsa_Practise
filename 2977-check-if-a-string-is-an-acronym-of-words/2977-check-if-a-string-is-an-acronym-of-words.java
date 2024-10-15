class Solution {
    public boolean isAcronym(List<String> words, String s) {
        int i =0; //for position in string 
        int n =s.length(); //string length
        if(n !=words.size()) return false; //if the size of acronym not matches the length of words 
        for(String word : words){
            if(word.charAt(0) != s.charAt(i++)) return false;

        }
        return true;
        
    }
}