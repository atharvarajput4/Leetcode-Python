class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case
        if(n==0 or n==1):
            return n
        # recurssive case
        return self.fib(n-1)+self.fib(n-2)
        