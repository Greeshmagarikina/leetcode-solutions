class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minCost=prices[0]
        for i in range(len(prices)):
            profit=max(prices[i]-minCost,profit)
            minCost=min(prices[i],minCost)
        return profit
