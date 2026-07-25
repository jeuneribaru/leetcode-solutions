class Solution:
    def maxProduct(self, n: int) -> int:
        str_n = str(n)
        if len(str_n) == 2 :
            return int(str_n[0])*int(str_n[1])
        else: 
            maxx = 0
            for i in range(0, len(str_n)) : 
                pro = int(str_n[i])
                for j in range(i+1, len(str_n)) :
                    pro *= int(str_n[j])
                if pro > maxx :
                    maxx = pro 
            return maxx
                    