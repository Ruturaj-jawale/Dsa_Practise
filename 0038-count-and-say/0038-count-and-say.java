class Solution {
    public String countAndSay(int n) {
        
    if(n == 1) return "1";

    String prev =countAndSay(n - 1);
    StringBuilder sb = new StringBuilder();

    int count = 1;
   

    for(int i = 1; i < prev.length(); i++){
        if(prev.charAt(i) == prev.charAt(i - 1)){
            count++;
        }else{
            sb.append(count).append(prev.charAt(i - 1));
            // currChar = prev.charAt(i);
            count = 1;
        }
    }
    sb.append(count).append(prev.charAt(prev.length() - 1));
    return sb.toString();
    }
}

// class Solution {
//     public String countAndSay(int n) {
//         // Base case
//         if (n == 1) return "1";
        
//         // Get the previous term recursively
//         String prev = countAndSay(n - 1);
//         StringBuilder sb = new StringBuilder();

//         int count = 1;
//         for (int i = 1; i < prev.length(); i++) {
//             if (prev.charAt(i) == prev.charAt(i - 1)) {
//                 count++;
//             } else {
//                 sb.append(count).append(prev.charAt(i - 1));
//                 count = 1;
//             }
//         }

//         // Don't forget the last group
//         sb.append(count).append(prev.charAt(prev.length() - 1));

//         return sb.toString();
//     }
// }
