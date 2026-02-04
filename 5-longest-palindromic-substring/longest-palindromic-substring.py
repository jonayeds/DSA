class Solution(object):
    def longestPalindrome(self, s):
        res= ''
        for i in range(len(s)):
            temp=s[i]
            if len(s)==1:
                res=temp
                continue
            if i==0:
                if s[i]==s[i+1]:
                    temp=temp+s[i+1]
            elif i==len(s)-1:
                if s[i] == s[i - 1]:
                    temp = temp + s[i - 1]
            elif  s[i - 1]==s[i + 1]:
                high=1
                low=1
                while i+high<len(s) and i-low>=0:
                    if s[i + high] != s[i - low]:
                        break
                    else:
                        temp = s[i - low] + temp + s[i + high]
                    high += 1
                    low += 1
            if  i < len(s)-2 and s[i] == s[i+1]:
                temp1= s[i]+ s[i+1]
                high=2
                low=1
                while i+high<len(s) and i-low>=0:
                    if s[i+high] != s[i - low]:
                        break
                    else:
                        temp1 = s[i - low] + temp1 + s[i+high]
                    high += 1
                    low += 1

                if len(temp1)>len(temp):
                    temp=temp1
            if s[i] == s[i-1]:
                temp1 = s[i] + s[i - 1]
                high=1
                low=2
                while i+high<len(s) and i-low>=0:
                    if s[i + high] != s[i-low]:
                        break
                    else:
                        temp1 = s[i -low] + temp1  + s[i + high]
                    high += 1
                    low += 1
                    if len(temp1)>len(temp):
                        temp=temp1
            if len(temp) > len(res):
                res=temp
        return res