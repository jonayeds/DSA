class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j=0,len(height)-1
        max_area=0
        while i<j:
            h=min(height[i],height[j])
            w=j-i
            area=h*w
            if area > max_area:
                max_area=area
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area