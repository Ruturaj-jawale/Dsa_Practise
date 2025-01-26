
class Solution {
    public int maximumInvitations(int[] favorite) {
        int n = favorite.length;

        // Step 1: Initialize arrays
        int[] inDegree = new int[n];  // Array to store in-degrees
        int[] depth = new int[n];    // Depth array to store chain lengths
        Queue<Integer> queue = new LinkedList<>();  // Queue for topological sorting

        // Step 2: Count in-degrees
        for (int i = 0; i < n; i++) {
            inDegree[favorite[i]]++;
        }

        // Step 3: Process chains using topological sorting
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) queue.add(i);  // Add nodes with in-degree 0
        }

        while (!queue.isEmpty()) {
            int current = queue.poll();  // Remove node from queue
            int next = favorite[current];  // Follow the edge to the next node
            depth[next] = Math.max(depth[next], depth[current] + 1);  // Update chain length
            if (--inDegree[next] == 0) {  // Reduce in-degree of the next node
                queue.add(next);
            }
        }

        // Step 4: Process cycles and calculate results
        boolean[] visited = new boolean[n];
        int maxCycleSize = 0;  // Maximum cycle length
        int chainContribution = 0;  // Sum of lengths of chains and 2-cycles

        for (int i = 0; i < n; i++) {
            if (!visited[i] && inDegree[i] > 0) {  // Node is part of a cycle
                int cycleLength = 0;
                int current = i;

                // Count cycle size and mark nodes as visited
                do {
                    visited[current] = true;
                    current = favorite[current];
                    cycleLength++;
                } while (current != i);

                if (cycleLength == 2) {  // Special case: 2-cycle
                    chainContribution += depth[i] + depth[favorite[i]] + 2;
                } else {  // Larger cycles
                    maxCycleSize = Math.max(maxCycleSize, cycleLength);
                }
            }
        }

        // Return the maximum result between largest cycle and 2-cycle chains
        return Math.max(maxCycleSize, chainContribution);
    }
}
