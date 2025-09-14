/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */

class Solution {
    public int findInMountainArray(int target, MountainArray arr) {
        int peak = peakIndex(arr);

        // Search in ascending part
        int firstTry = binarySearch(arr, target, 0, peak, true);
        if (firstTry != -1) return firstTry;

        // Search in descending part
        return binarySearch(arr, target, peak + 1, arr.length() - 1, false);
    }

    // Find peak index using binary search
    public int peakIndex(MountainArray arr) {
        int start = 0;
        int end = arr.length() - 1;

        while (start < end) {
            int mid = start + (end - start) / 2;
            if (arr.get(mid) < arr.get(mid + 1)) {
                start = mid + 1; // go right
            } else {
                end = mid; // go left
            }
        }
        return start;
    }

    // Unified binary search (works for both asc & desc order)
    public int binarySearch(MountainArray arr, int target, int start, int end, boolean isAsc) {
        while (start <= end) {
            int mid = start + (end - start) / 2;
            int value = arr.get(mid);

            if (value == target) return mid;

            if (isAsc) {
                if (value < target) start = mid + 1;
                else end = mid - 1;
            } else {
                if (value > target) start = mid + 1;
                else end = mid - 1;
            }
        }
        return -1;
    }
}
