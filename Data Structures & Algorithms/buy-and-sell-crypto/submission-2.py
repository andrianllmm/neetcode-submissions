class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0

        max_profit = 0
        buy, sell = 0, 1

        while sell < n:
            if prices[sell] - prices[buy] > max_profit:
                max_profit = prices[sell] - prices[buy]
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1

        return max_profit