class Solution(object):
    def containsDuplicate(self, nums):
        dic={}
        for i in nums:
            if dic.get(i) is None:
                dic[i]=True
            else:
                return True
        return False