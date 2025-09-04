class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        indx=0
        for i in range(0,n,1):
            if(nums[i]%2 == 0):
                temp = nums[i]
                nums[i]=nums[indx]
                nums[indx]=temp
                indx+=1
        return nums
                
        