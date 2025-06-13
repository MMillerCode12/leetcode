public class Solution {
    public int MaxProfit(int[] prices) {
        int max_profit = 0;
        int left = 0;

        for (int right = 0; right < prices.Length; right++) {
            if (right == left) {
                continue;
            }

            if (prices[right] > prices[left]) {
                var temp_prof = prices[right] - prices[left];

                if (temp_prof > max_profit) {
                    max_profit = temp_prof;
                }
            } else if (prices[right] < prices[left]) {
                left = right;
            }

        }

        return max_profit;
    }
}
