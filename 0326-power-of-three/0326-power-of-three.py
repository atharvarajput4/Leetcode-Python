class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #base case
        if(n == 1):
            return True
        if(n <= 0):
            return False
        if(n%3!=0):
            return False
        #recurssive case
        return self.isPowerOfThree(n//3)

        