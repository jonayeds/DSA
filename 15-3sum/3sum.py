class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        nums_registry=[]
        for i in range(len(nums)):
            if nums[i]>0:break
            if i > 0 and  nums[i]== nums[i - 1]:
                continue
            j=i+1
            k=len(nums)-1
            el_i=nums[i]
            while j<k:
                el_j=nums[j]
                el_k=nums[k]
                total=el_i+el_j+el_k
                if total==0:
                    nums_registry.append([el_i, el_j, el_k])
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif total>0:
                    k-=1
                elif total<0:
                    j+=1
                    
        return nums_registry