class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #base case
        if(n<=0):
            return False
        if(n==1):
            return True
        if(n%2!=0):
            return False
        #recurssive case
        return self.isPowerOfTwo(n//2)

        