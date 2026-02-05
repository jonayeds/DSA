class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rng=len(nums)-1
        temp=[]
        for j in nums:
            temp.append(j)
        count =1
        for i in range(rng):
            if temp[i]==temp[i+1]:
                nums[i]='_'
                nums.append("_")
            else:
                count+=1
        max_el=temp[rng]
        i=0
        while nums[i]!=max_el:
            if nums[i]=='_':
                del nums[i]
            else:
                i+=1
        return count
