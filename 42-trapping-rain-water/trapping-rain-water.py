class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_max=[]
        r_max=[]
        min_lr=[]
        for i in range(len(height)):
            l=len(height)-1
            if i==0:
                l_max.append(0)
                r_max.append(0)
            else:
                m=max(l_max[i-1],height[i-1])
                n=max(r_max[0], height[l-i+1])
                l_max.append(m)
                r_max.insert(0,n)



        output=0
        for i in range(1,len(height)-1):
            l_p=height[i]<l_max[i]
            r_p=height[i]<r_max[i]
            if l_p and r_p:
                diff=min(l_max[i],r_max[i])-height[i]
                output+=diff
        return output