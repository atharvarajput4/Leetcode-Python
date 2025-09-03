class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #for -ve case
        if n<0:
            x=1/x
            n=-n
        #base case
        if(n==0):
            return 1
        #recurssive case
        a = self.myPow(x,n//2) 
        if(n%2==0):
            return a*a
        else:
            return a*a*x

        