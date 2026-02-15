class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        window=1
        max_window=1
        table={}
        for i in range(65, 65+26):
            table[chr(i)]=0
        i=j=0
        table[s[0]]=1
        while j<len(s):
            most_freq=max(table.values())
            if window-most_freq<=k:
                max_window=max(window, max_window)
                window+=1
                j+=1
                if j<len(s):
                    table[s[j]]+=1
            else:
                window-=1
                if i<len(s)-1:
                    table[s[i]]-=1
                i+=1
        return max_window