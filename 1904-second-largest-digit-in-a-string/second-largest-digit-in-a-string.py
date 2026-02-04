class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            '0':0
        }
        i=0
        largest=-1
        res=-1
        while i<len(s):
            num=dic.get(s[i])
            if num is not None:
                if num>largest:
                    res=largest
                    largest=num
                elif res<num<largest:
                    res=num
            i+=1

        return res