class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size= len(prices)
        profit = 0
        for buy in range(size-1):
            for sell in range(buy+1, size):
                if prices[buy] < prices[sell]:
                    profit = max(profit, prices[sell]-prices[buy])
                sell -= 1
        return profit