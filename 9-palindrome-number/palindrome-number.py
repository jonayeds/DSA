class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        print(s)
        for i in range(len(s)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
        