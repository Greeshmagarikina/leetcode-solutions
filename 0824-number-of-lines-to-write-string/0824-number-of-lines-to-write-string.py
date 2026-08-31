class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines=1
        curr=0
        for char in s:
            width=widths[ord(char)-ord('a')]
            if curr+width<=100:
                curr+=width
            else:
                lines+=1
                curr=width
        return [lines,curr]