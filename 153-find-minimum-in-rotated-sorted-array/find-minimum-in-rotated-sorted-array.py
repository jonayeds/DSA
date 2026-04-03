from math import ceil
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        start=0
        end = len(nums)-1
        while start<=end:
            mid = ceil((start+end)/2)
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[mid]<nums[start]:
                end=mid
            elif nums[mid]>nums[end]:
                start=mid
            else:
                break
        return nums[0]