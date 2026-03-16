from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices=[]
        result_stack=[]
        output=[0 for i in range(len(temperatures))]
        result_stack.append(temperatures[0])
        indices.append(0)
        for i in range(1, len(temperatures)):
            temp=temperatures[i]
            top=result_stack[len(result_stack)-1]
            indices.append(i)
            result_stack.append(temp)
            while temp>top and len(result_stack)>0:
                result_stack.pop(len(result_stack)-2)
                output[indices[len(result_stack)-1]]=i-indices[len(indices)-2]
                indices.pop(len(indices)-2)
                if len(result_stack)>1:
                    top = result_stack[len(result_stack)-2]
                else:
                    break
        return output
