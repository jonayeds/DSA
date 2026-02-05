class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dic={}
        for i in range(len(s)):
            arr=dic.get(s[i])
            if arr is None:
                dic[s[i]] = [i]
            else:
                arr.append(i)
        for t_chr in t:
            lst=dic.get(t_chr)
            if lst is not  None:
                del lst[0]
                if len(lst)==0:
                    dic[t_chr]=None
            else:
                return False
        return True