import java.util.PriorityQueue;

class Solution {
    public String longestDiverseString(int a, int b, int c) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((x, y) -> y[0] - x[0]);

        // Add character counts to the heap, character is stored as ASCII value
        if (a > 0) maxHeap.offer(new int[]{a, 'a'});
        if (b > 0) maxHeap.offer(new int[]{b, 'b'});
        if (c > 0) maxHeap.offer(new int[]{c, 'c'});

        StringBuilder result = new StringBuilder();

        while (!maxHeap.isEmpty()) {
            int[] first = maxHeap.poll();
            char char1 = (char) first[1];

            // Check if we can append this character without making three consecutive characters
            if (result.length() > 1 && result.charAt(result.length() - 1) == char1 && result.charAt(result.length() - 2) == char1) {
                // If we cannot add the character, try to use the second most frequent character
                if (maxHeap.isEmpty()) break;  // No other characters available
                
                int[] second = maxHeap.poll();
                char char2 = (char) second[1];
                
                // Append the second character and decrement its count
                result.append(char2);
                second[0]--;

                // Re-add the second character back into the heap if it has remaining counts
                if (second[0] > 0) {
                    maxHeap.offer(second);
                }
                // Put the first character back into the heap for future use
                maxHeap.offer(first);
            } else {
                // Append the first character and decrement its count
                result.append(char1);
                first[0]--;

                // Re-add the first character back into the heap if it has remaining counts
                if (first[0] > 0) {
                    maxHeap.offer(first);
                }
            }
        }

        return result.toString();
    }
}
