class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = len(s)-1
        if " " not in s :
            return len(s)
        while i > 0 and s[i] != " " :
            i -= 1
        ret = 0
        for j in range(i+1, len(s)) :
                ret += 1
        return ret 

