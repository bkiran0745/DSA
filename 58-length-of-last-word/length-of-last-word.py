class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        j = 0
        for i in s[::-1]:
            if j == 0 and not i.isalpha():
                continue
            elif i.isalpha():
                j += 1
            elif not i.isalpha():
                break
        return j