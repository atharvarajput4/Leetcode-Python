class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0]*n
        for i in range(0,n):
            if(i==0):
                ans[i]=nums[i]
            else:
                ans[i]=ans[i-1]+nums[i]
        
        return ans

        