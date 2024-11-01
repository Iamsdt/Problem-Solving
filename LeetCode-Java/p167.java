class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int p = 0;
        int n = numbers.length - 1;

        while (p < n) {
            int sum = numbers[p] + numbers[n];
            
            if (sum == target) {
                return new int[]{p + 1, n + 1};  // 1-based indexing
            }

            if (sum < target) {
                p++;
            } else {
                n--;
            }
        }

        return new int[]{-1, -1};
    }
}