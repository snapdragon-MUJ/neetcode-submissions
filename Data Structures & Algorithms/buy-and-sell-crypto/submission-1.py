class Solution:

  def maxProfit(self, prices: list[int]) -> int:
    maxProfit=0
    n=len(prices)
    for i in range(0,n):
      for j in range(i+1,n):
        if prices[j]-prices[i]>maxProfit:
          maxProfit= prices[j]-prices[i]
    return maxProfit