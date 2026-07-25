class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result=[]
        for word in words:
            chars=word.split(separator)
            for char in chars:
                if char:
                    result.append(char)
        return result
