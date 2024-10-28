class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        
        left = 0
        for right in range(len(prices)):
            profit = prices[right]  - prices[left]
            max_profit = max(max_profit,profit)

            if profit < 0:
                left = right
            
        print(\reached here\,max_profit)       

        return max(max_profit,0)