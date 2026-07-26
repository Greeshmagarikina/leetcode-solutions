class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=[]
        n1=len(word1)
        n2=len(word2)
        maximum=max(n1,n2)
        for i in range(maximum):
            if i<n1:
                result.append(word1[i])
            if i<n2:
                result.append(word2[i])
        return "".join(result)
