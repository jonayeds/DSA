class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        dic={}
        temp=0
        i=0
        for c in s:
            if dic.get(c) is None:
                dic[c]=i
                i+=1
                temp+=1
            else:
                serial=dic.get(c)
                j=i
                dic={}
                while j>serial:
                    dic[s[j]]=j
                    j-=1
                i+=1

                temp=i-serial-1
            count = max(temp, count)

        return count