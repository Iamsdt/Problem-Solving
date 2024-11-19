
public class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        if (sum(nums) < target) return 0;

        int s = 0, l = 0, ans = nums.length;

        for (int r = 0; r < nums.length; r++) {
            s += nums[r];
            while (s >= target) {
                s -= nums[l];
                ans = Math.min(ans, r - l + 1);
                l++;
            }
        }

        return ans;
    }

    private int sum(int[] nums) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        return total;
    }
}