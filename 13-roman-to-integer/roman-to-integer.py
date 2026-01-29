class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        total=0
        i=0
        sub_sum=0
        while i < len(s):
            current_num=roman.get(s[i])
            if i<len(s)-1:
                next_num = roman.get(s[i+1])
                if next_num <= current_num:
                    total+=current_num
                else:
                    total-=current_num
            else:
                total+=current_num

            i+=1
        return total



