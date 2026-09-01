class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sin,tin=0,0
        while sin<len(s) and tin<len(t):
            if s[sin]==t[tin]:
                sin+=1
            tin+=1
        return sin==len(s)