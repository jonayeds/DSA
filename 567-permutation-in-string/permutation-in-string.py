class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_count={chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        s2_count={chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        matches=0
        if len(s1)>len(s2): return False
        for k in range(len(s1)):
            s2_count[s2[k]]+=1
            s1_count[s1[k]]+=1

        for i in range(ord('a'), ord('z')+1):
            char=chr(i)
            matches+=(1 if s1_count[char] == s2_count[char] else 0)

        i=len(s1)

        while i<len(s2):
            if matches == 26:
                return True
            prev_chr=s2[i-len(s1)]
            current_chr=s2[i]
            s2_count[current_chr]+=1
            if s1_count[current_chr]==s2_count[current_chr]:
                matches+=1
            elif s1_count[current_chr]+1==s2_count[current_chr]:
                matches-=1

            s2_count[prev_chr]-=1
            if s1_count[prev_chr]==s2_count[prev_chr]:
                matches+=1
            elif s1_count[prev_chr]-1==s2_count[prev_chr]:
                matches-=1
            i+=1
        return matches==26