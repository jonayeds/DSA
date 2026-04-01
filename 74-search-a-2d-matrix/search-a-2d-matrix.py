from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix[0])
        n=len(matrix)
        c_s=0
        c_e=m*n
        c=int(c_s+((c_e-c_s)/2))
        mid = (int(c/m), int(c%m))
        while c!=0 and c_e!=c_s+1:
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]]>target:
                c_e=c
                c= int(c_s+((c_e-c_s)/2))
                mid=(int(c/m), int(c%m))
            else:
                c_s=c
                c=int(c_s+((c_e-c_s)/2))
                mid =(int(c/m), int(c%m))
        if c_e==1 and c==0:
            return matrix[0][0]==target

        return False