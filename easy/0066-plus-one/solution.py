class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ""
        for chiffre in digits : 
            s+=str(chiffre)
        l = []
        for char in str(int(s)+1) :
            l.append(int(char))
        return l




        