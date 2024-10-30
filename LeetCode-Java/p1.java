import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum2(int[] nums, int target) {
        int head = 0;
        int cu = 1;
        
        while (head < nums.length) {
            if ((nums[head] + nums[cu]) == target) {
                return new int[]{head, cu};
            }
            
            if (cu == nums.length - 1) {
                head += 1;
                cu = head + 1;
            } else {
                cu += 1;
            }
        }
        return new int[]{0, 0};
    }

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        
        return new int[]{0, 0};
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] result = solution.twoSum2(new int[]{2, 7, 11, 15}, 9);
        System.out.println("[" + result[0] + ", " + result[1] + "]");
    }
}