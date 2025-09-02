class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #base case
        if(n == 1):
            return True
        if(n <= 0):
            return False
        if(n%4!=0):
            return False
        #recurssive case
        return self.isPowerOfFour(n//4)