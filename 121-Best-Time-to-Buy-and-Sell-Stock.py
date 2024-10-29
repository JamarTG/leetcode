class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        
        left = 0
        # iterate through prices
        for right in range(len(prices)):
            # calculate profit
            profit = prices[right]  - prices[left]
            # update max profit
            max_profit = max(max_profit,profit)

            # if unprofitable
            if profit < 0:
                # set new lowest price index
                left = right
        # no negative profits
        return max(max_profit,0)
