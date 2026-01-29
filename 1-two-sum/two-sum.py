class Solution(object):
    def twoSum(self, nums, target):
        first, second = 0, 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    first=i,
                    second=j
                    return [i,j]
        if first==second:
            return None
        else:
            return [first,second]
        