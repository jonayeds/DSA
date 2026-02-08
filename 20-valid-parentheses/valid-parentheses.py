class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        recent=[]
        ref={
            '}':"{",
            ')':'(',
            ']':'['
        }
        if len(s)%2 == 1:
            return False

        for i in range(len(s)):
            x=s[i]
            el=ref.get(x)
            if el is None:
                recent.append(s[i])
            else:
                if len(recent)==0 or el!=recent[len(recent)-1]:
                    return False
                else:
                    recent.pop()
        if len(recent)>0:return False
        return True
