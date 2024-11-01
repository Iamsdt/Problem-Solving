class Solution {
    public int maxArea(int[] height) {
        int p = 0;
        int q = height.length - 1;
        int maxArea = 0;

        while (p < q) {
            // Calculate the area with the current two pointers
            int area = Math.min(height[p], height[q]) * (q - p);
            maxArea = Math.max(maxArea, area);

            // Update the pointer with the shorter height
            if (height[p] < height[q]) {
                p++;
            } else {
                q--;
            }
        }

        return maxArea;
    }
}