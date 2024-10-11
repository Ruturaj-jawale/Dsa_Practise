public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure that nums1 is the smaller array for optimization
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.length;
        int n = nums2.length;
        int halfLen = (m + n + 1) / 2;

        int left = 0, right = m;

        while (left <= right) {
            int i = (left + right) / 2;  // Partition index for nums1
            int j = halfLen - i;  // Partition index for nums2

            // Check boundary conditions
            int nums1Left = (i > 0) ? nums1[i - 1] : Integer.MIN_VALUE;
            int nums1Right = (i < m) ? nums1[i] : Integer.MAX_VALUE;
            int nums2Left = (j > 0) ? nums2[j - 1] : Integer.MIN_VALUE;
            int nums2Right = (j < n) ? nums2[j] : Integer.MAX_VALUE;

            if (nums1Left <= nums2Right && nums2Left <= nums1Right) {
                // Correct partition found
                if ((m + n) % 2 == 1) {
                    // If the total length is odd, return the max of the left parts
                    return Math.max(nums1Left, nums2Left);
                } else {
                    // If the total length is even, return the average of the middle elements
                    return (Math.max(nums1Left, nums2Left) + Math.min(nums1Right, nums2Right)) / 2.0;
                }
            } else if (nums1Left > nums2Right) {
                // Move towards the left in nums1
                right = i - 1;
            } else {
                // Move towards the right in nums1
                left = i + 1;
            }
        }

        // If no solution is found, return an error (though this should never happen)
        throw new IllegalArgumentException("Input arrays are not valid.");
    }

    
}
