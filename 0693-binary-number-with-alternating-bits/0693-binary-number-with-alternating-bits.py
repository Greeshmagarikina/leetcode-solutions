class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        result=n^(n>>1)
        return (result & (result+1))==0