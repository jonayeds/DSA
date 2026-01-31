class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        total=0
        valid_sum=0
        for i in range(n):
            total+=nums[i]
        for j in range(n+1):
            valid_sum+=j
        return valid_sum-total