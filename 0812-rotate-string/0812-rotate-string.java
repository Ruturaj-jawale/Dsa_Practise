class Solution {
    public boolean rotateString(String s, String goal) {
       BiFunction< String, String, Boolean > isRoatation = (str, target) ->
       str.length() == target.length() && (str+str).contains(target);
        return isRoatation.apply(s, goal);
    }
}