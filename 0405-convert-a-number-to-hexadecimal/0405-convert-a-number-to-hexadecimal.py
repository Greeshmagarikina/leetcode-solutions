class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        hex_map="0123456789abcdef"
        if num<0:
            num&=0XFFFFFFFF
        result=[]
        while num>0:
            remainder=num%16
            result.append(hex_map[remainder])
            num//=16
        return "".join(reversed(result))