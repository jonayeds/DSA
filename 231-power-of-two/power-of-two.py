class Solution(object):
    def isPowerOfTwo(self, n):
        if n==1:
            return True
        else:
            parameter=1
            while parameter<=n:
                if parameter==n:
                    return True
                else:
                    parameter*=2
            return False