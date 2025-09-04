class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if(n <=2):
            return n
        start=1
        for i in range(2,n,1):
            if(nums[i] != nums[start-1]):
                start+=1
                nums[start]=nums[i]
        return start+1
        