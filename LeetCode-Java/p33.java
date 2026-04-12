class Solution {
    public int search(int[] nums, int target) {
        int p = 0;
        int q = nums.length - 1;
        
        while (p <= q) {
            int m = (p + q) / 2;
            
            if (nums[m] == target) {
                return m;
            } else if (nums[m] >= nums[p]) {
                if (nums[p] <= target && target <= nums[m]) {
                    q = m - 1;
                } else {
                    p = m + 1;
                }
            } else {
                if (nums[m] <= target && target <= nums[q]) {
                    p = m + 1;
                } else {
                    q = m - 1;
                }
            }
        }
        
        return -1;
    }
}
