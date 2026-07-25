class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I' : 1, 
            'V' : 5, 
            'X' : 10, 
            'L': 50, 
            'C': 100, 
            'D' : 500, 
            'M' : 1000
        }
        for i in range(len(s)): 
        ret = 0
            ret += dic[s[i]] 
        for j in range(1,len(s)) :
            if s[i-1] == "I" and ([i] == "V" or s[i] == "X"):
                    ret -= 2

            elif s[i-1] == "X" and ([i] == "L" or s[i] == "C"):
                    ret -= 10
            elif s[i-1] == "C" and ([i] == "D" or s[i] == "M"):
                    ret -= 100
        return ret 

