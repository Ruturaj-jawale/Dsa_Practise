import java.util.*;

class Router {
    private static class Packet {
        int source, destination, timestamp;
        Packet(int s, int d, int t) {
            source = s; destination = d; timestamp = t;
        }
    }

    private int memoryLimit;
    private Deque<Packet> queue;
    private Set<String> packetSet;
    private Map<Integer, ArrayList<Integer>> destMap;

    public Router(int memoryLimit) {
        this.memoryLimit = memoryLimit;
        this.queue = new LinkedList<>();
        this.packetSet = new HashSet<>();
        this.destMap = new HashMap<>();
    }

    private String makeKey(int s, int d, int t) {
        return s + "#" + d + "#" + t;
    }

    private Packet removeOldest() {
        if (queue.isEmpty()) return null;
        Packet pkt = queue.pollFirst();
        packetSet.remove(makeKey(pkt.source, pkt.destination, pkt.timestamp));

        ArrayList<Integer> arr = destMap.get(pkt.destination);
        if (arr != null) {
            // oldest timestamps are always at the front
            if (!arr.isEmpty() && arr.get(0) == pkt.timestamp) {
                arr.remove(0);
            } else {
                // fallback if not front (rare case)
                int idx = Collections.binarySearch(arr, pkt.timestamp);
                if (idx >= 0) arr.remove(idx);
            }
            if (arr.isEmpty()) destMap.remove(pkt.destination);
        }
        return pkt;
    }

    public boolean addPacket(int source, int destination, int timestamp) {
        String key = makeKey(source, destination, timestamp);
        if (packetSet.contains(key)) return false;

        if (queue.size() >= memoryLimit) {
            removeOldest(); // evict
        }

        Packet pkt = new Packet(source, destination, timestamp);
        queue.addLast(pkt);
        packetSet.add(key);

        destMap.computeIfAbsent(destination, k -> new ArrayList<>()).add(timestamp);
        return true;
    }

    public int[] forwardPacket() {
        Packet pkt = removeOldest();
        if (pkt == null) return new int[0];
        return new int[]{pkt.source, pkt.destination, pkt.timestamp};
    }

    public int getCount(int destination, int startTime, int endTime) {
        if (!destMap.containsKey(destination)) return 0;
        ArrayList<Integer> arr = destMap.get(destination);

        int left = lowerBound(arr, startTime);
        int right = upperBound(arr, endTime);
        return right - left;
    }

    // Binary search helpers
    private int lowerBound(ArrayList<Integer> arr, int target) {
        int lo = 0, hi = arr.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr.get(mid) < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    private int upperBound(ArrayList<Integer> arr, int target) {
        int lo = 0, hi = arr.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr.get(mid) <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
