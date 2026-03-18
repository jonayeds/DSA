from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[[p,s] for p,s in zip(position,speed)]
        stack=[]
        stack.append(max(pair, key= lambda x:x[0]))
        for p,s in sorted(pair, key= lambda x: -x[0])[1:]:
            time_taken=(target-p)/s
            top_p, top_s=stack[len(stack)-1]
            time_taken_prev=(target-top_p)/top_s
            if time_taken>time_taken_prev:
                stack.append([p,s])


        return len(stack)
