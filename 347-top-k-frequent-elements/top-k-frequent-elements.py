class Solution(object):
    def topKFrequent(self, nums, k):
        n=0
        freq={}
        for i in nums:
            elem=freq.get(i)
            if elem is None:
                freq[i]=1
            else:
                freq[i]+=1
        vals=list(freq.values())
        keys=list(freq.keys())
        res={}
        for j in range(len(vals)):
            val=vals[j]
            key=keys[j]
            el=res.get(val)
            if el is None:
                res[val]=[key]
            else:
                res[val].append(key)
        ks=list(res.keys())
        m=sorted(ks,reverse=True)
        result_arr=[]
        i = 0
        while n<k:
            arr=res.get(m[i])
            result_arr.append(arr[0])
            if len(arr)<=1:
                del arr
                i+=1
            else:
                del arr[0]
            n+=1

        return result_arr
