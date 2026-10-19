class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -1
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    profit = max(profit, prices[j]-prices[i])
        return profit if profit > 0 else 0