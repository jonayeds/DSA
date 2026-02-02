class Solution(object):
    def longestConsecutive(self, nums):
        dic= dict(zip(nums, range(len(nums))))
        count=n=0
        while n<len(nums):
            temp=1
            if len(dic)==0:
                break
            key = next(iter(dic))
            n+=1
            del dic[key]
            a=key
            while dic.get(a - 1) is not None:
                temp+=1
                n+=1
                a-=1
                del dic[a]
            a=key
            while dic.get(a+1) is not None:
                temp+=1
                n+=1
                a+=1
                del dic[a]

            count=max(temp,count)
        return count
