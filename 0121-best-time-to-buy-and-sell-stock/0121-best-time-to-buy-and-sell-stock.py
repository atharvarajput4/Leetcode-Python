class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = nums[0]
        for i in range(1,len(nums),1):
            current_profit = nums[i] - min_price
            if (profit < current_profit):
                profit = current_profit
            if(nums[i] < min_price):
                min_price = nums[i]
        return profit
        