class Solution {
    public void moveZeroes(int[] nums) {
        int m = 0;
        int n = 1;
        
        while (m < nums.length && n < nums.length) {
            if (nums[n] == 0 && nums[m] == 0) {
                n++;
                continue;
            }
            
            if (nums[m] == 0) {
                int temp = nums[m];
                nums[m] = nums[n];
                nums[n] = temp;
            }
            
            n++;
            m++;
        }
    }
}
