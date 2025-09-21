import java.util.*;

class MovieRentingSystem {
    private Map<List<Integer>, Integer> price; // (shop, movie) -> price
    private Map<Integer, TreeSet<int[]>> available; // movie -> available copies {price, shop}
    private TreeSet<int[]> rented; // all rented movies {price, shop, movie}

    // Comparators
    private Comparator<int[]> cmpAvail = (a, b) -> {
        if (a[0] != b[0]) return a[0] - b[0]; // sort by price
        return a[1] - b[1];                   // then by shop
    };

    private Comparator<int[]> cmpRented = (a, b) -> {
        if (a[0] != b[0]) return a[0] - b[0]; // sort by price
        if (a[1] != b[1]) return a[1] - b[1]; // then by shop
        return a[2] - b[2];                   // then by movie
    };

    public MovieRentingSystem(int n, int[][] entries) {
        price = new HashMap<>();
        available = new HashMap<>();
        rented = new TreeSet<>(cmpRented);

        for (int[] e : entries) {
            int shop = e[0], movie = e[1], p = e[2];
            price.put(Arrays.asList(shop, movie), p);
            available.putIfAbsent(movie, new TreeSet<>(cmpAvail));
            available.get(movie).add(new int[]{p, shop});
        }
    }

    public List<Integer> search(int movie) {
        List<Integer> res = new ArrayList<>();
        if (!available.containsKey(movie)) return res;

        Iterator<int[]> it = available.get(movie).iterator();
        int k = 0;
        while (it.hasNext() && k < 5) {
            res.add(it.next()[1]); // shop id
            k++;
        }
        return res;
    }

    public void rent(int shop, int movie) {
        int p = price.get(Arrays.asList(shop, movie));
        // remove from available
        available.get(movie).remove(new int[]{p, shop});
        // add to rented
        rented.add(new int[]{p, shop, movie});
    }

    public void drop(int shop, int movie) {
        int p = price.get(Arrays.asList(shop, movie));
        // remove from rented
        rented.remove(new int[]{p, shop, movie});
        // add back to available
        available.get(movie).add(new int[]{p, shop});
    }

    public List<List<Integer>> report() {
        List<List<Integer>> res = new ArrayList<>();
        Iterator<int[]> it = rented.iterator();
        int k = 0;
        while (it.hasNext() && k < 5) {
            int[] cur = it.next();
            res.add(Arrays.asList(cur[1], cur[2])); // [shop, movie]
            k++;
        }
        return res;
    }
}
