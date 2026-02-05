class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        rng=len(nums)
        count=0
        i=0
        while i<rng:
            if nums[i]!='_':
                if nums[i]==val:
                    del nums[i]
                    nums.append('_')
                else:
                    i+=1
                    count+=1
            else:
                i+=1
        return count