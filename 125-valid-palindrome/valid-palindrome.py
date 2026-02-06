class Solution(object):
    def isPalindrome(self, s):

        str_arr=list(s)
        i=0
        while i<len(str_arr):
            code=ord(str_arr[i])
            if  65<= code <=90:
                str_arr[i] =str_arr[i].lower()
                i+=1
            elif 97<= code <= 122 or 48<= code <= 57:
                i+=1
            else:
                del str_arr[i]
        for i in range(int(len(str_arr)/2)):
            if str_arr[i] != str_arr[len(str_arr)-i-1]:
                return False
        return True