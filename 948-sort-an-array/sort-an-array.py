class Solution(object):
    def merge(self, nums, start, mid, end):
        temp=[]
        i=start
        j=mid+1
        while i<=mid and j<=end:
            if nums[i]<=nums[j]:
                temp.append(nums[i])
                i+=1
            else:
                temp.append(nums[j])
                j+=1
        while i<=mid:
            temp.append(nums[i])
            i+=1
        while j<=end:
            temp.append(nums[j])
            j+=1
        for k in range(len(temp)):
            nums[k+start]= temp[k]



    def merge_sort(self, nums, start, end):
        if start<end:
            mid=int(start+ (end-start)/2)
            Solution.merge_sort(self,nums,start,mid)
            Solution.merge_sort(self,nums,mid+1,end)
            Solution.merge(self,nums,start,mid,end)


    def sortArray(self, nums):
        start=0
        end=len(nums)-1
        Solution.merge_sort(self,nums, start, end)
        return nums