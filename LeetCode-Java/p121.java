import java.util.List;

class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length < 2) {
            return 0;
        }
        
        int profit = 0;
        int invest = prices[0];
        
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < invest) {
                invest = prices[i];
            } else {
                profit = Math.max(prices[i] - invest, profit);
            }
        }
        
        return profit;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] prices = {2, 4, 1};
        System.out.println(sol.maxProfit(prices));
    }
}