class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        while i > 0 and s[i] != " " :
            i -= 1
        ret = -1
        for j in range(i, len(s)) :
                ret += 1

        return ret 
            if s[j] != " " :

