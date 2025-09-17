import java.util.*;

class FoodRatings {

    // Map food name -> [rating, cuisine]
    private Map<String, int[]> foodMap;
    // Map cuisine -> TreeSet of foods sorted by rating desc, then name asc
    private Map<String, TreeSet<String>> cuisineMap;
    // Comparator to sort by rating descending, then lexicographically ascending
    private Comparator<String> foodComparator;

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        foodMap = new HashMap<>();
        cuisineMap = new HashMap<>();
        
        foodComparator = (f1, f2) -> {
            int r1 = foodMap.get(f1)[0];
            int r2 = foodMap.get(f2)[0];
            if (r1 != r2) return r2 - r1; // higher rating first
            return f1.compareTo(f2);       // lexicographically smaller first
        };

        for (int i = 0; i < foods.length; i++) {
            foodMap.put(foods[i], new int[]{ratings[i], i}); // store index temporarily
            cuisineMap.putIfAbsent(cuisines[i], new TreeSet<>(foodComparator));
        }

        for (int i = 0; i < foods.length; i++) {
            foodMap.get(foods[i])[1] = cuisines[i].hashCode(); // store cuisine hash temporarily
            cuisineMap.get(cuisines[i]).add(foods[i]);
        }
    }
    
    public void changeRating(String food, int newRating) {
        // get cuisine
        int cuisineHash = foodMap.get(food)[1];
        String cuisine = null;
        for (String c : cuisineMap.keySet()) {
            if (c.hashCode() == cuisineHash) {
                cuisine = c;
                break;
            }
        }
        
        TreeSet<String> set = cuisineMap.get(cuisine);
        set.remove(food);               // remove old
        foodMap.get(food)[0] = newRating; // update rating
        set.add(food);                  // add back with new rating
    }
    
    public String highestRated(String cuisine) {
        return cuisineMap.get(cuisine).first(); // highest-rated food
    }
}


/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param_2 = obj.highestRated(cuisine);
 */