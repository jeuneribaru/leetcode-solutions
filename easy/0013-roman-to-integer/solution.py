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
            if s[j-1] == "I" and (s[j] == "V" or s[j] == "X"):
                    ret -= 2

            elif s[j-1] == "X" and (s[j] == "L" or s[j] == "C"):
                    ret -= 20
            elif s[j-1] == "C" and (s[j] == "D" or s[j] == "M"):
                    ret -= 200
        return ret 

