class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        min_amt = 9999999999999

        for i in prices:
            if i < min_amt:
                min_amt = i
            elif (i - min_amt) > profit:
                profit = i - min_amt


        return profit
        
