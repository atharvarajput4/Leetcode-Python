class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_sum=0
        for i in range(len(accounts)):
            sum=0
            for j in range(len(accounts[i])):
                sum+=accounts[i][j]
            if(max_sum < sum):
                max_sum=sum
        return max_sum

        
        