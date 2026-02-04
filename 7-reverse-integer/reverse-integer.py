class Solution(object):
    def reverse(self, x):
        if -2**31 <= x <= 2**31-1:
            str_num=str(x)
            reversed_num=''
            start=0
            if str_num[0]=='-':
                start=1
            for i in range(start,len(str_num)):
                reversed_num= str_num[i] + reversed_num
            if start ==1:
                reversed_num='-'+reversed_num
            int_reversed=int(reversed_num)
            if -2**31 <= int_reversed <= 2**31-1:
                return int_reversed
            else: return 0
        else:
            return 0