class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars=set()
        count=0
        for char in s:
            if char in chars:
                chars.remove(char)
                count+=1
            else:
                chars.add(char)
        return count*2+(1 if chars else 0)