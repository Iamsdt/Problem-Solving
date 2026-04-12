class Solution {
    public int maxSubArray(int[] nums) {
        int maxRes = nums[0];
        int current = 0;
        
        for (int num : nums) {
            if (current < 0) {
                current = 0;
            }
            current += num;
            maxRes = Math.max(maxRes, current);
        }
        
        return maxRes;
    }
}
