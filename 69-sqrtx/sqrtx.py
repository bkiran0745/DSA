class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        guess = x // 2
        while True:
            better_guess = (guess + x // guess) // 2
            if better_guess >= guess:
                return guess
            guess = better_guess