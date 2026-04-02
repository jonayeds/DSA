from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1
        end=max(piles)
        k=end
        while start<=end:
            mid=int((start+end)/2)
            total_time=0
            for p in piles:
                total_time+=ceil(p/mid)
            if total_time>h:
                start=mid+1
            else:
                end=mid-1
                k=mid
        return k
