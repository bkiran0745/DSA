class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
             
        prev2 = 1  
        prev1 = 2  
        i = 3
        while i <= n:
            current = prev1 + prev2
            prev2 = prev1    
            prev1 = current  
            i += 1           
            
        return prev1