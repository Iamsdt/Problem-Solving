class Solution {
    public int maxProduct(int[] nums) {
        int res = nums[0];
        int curMin = 1, curMax = 1;
        
        for (int n : nums) {
            if (n == 0) {
                curMin = 1;
                curMax = 1;
                continue;
            }
            
            int temp = n * curMax;
            curMax = Math.max(n * curMax, n * curMin);
            curMax = Math.max(curMax, n);
            curMin = Math.min(temp, n * curMin);
            curMin = Math.min(curMin, n);
            res = Math.max(res, curMax);
        }
        
        return res;
    }
}
