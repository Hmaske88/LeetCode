class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        diff=0
        for i in range(1,len(prices)):
            diff=max(diff,prices[i]-minPrice)
            minPrice=min(prices[i],minPrice)
        return diff
