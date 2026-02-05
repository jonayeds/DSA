class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                left_product[i]=1
                continue
            left_product[i]=left_product[i-1]*nums[i-1]
        right_product=1
        n=len(nums)
        for i in range(n):
            m=n-i-1
            left_product[m]=right_product*left_product[m]
            right_product=nums[m]*right_product


        return left_product