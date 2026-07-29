from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        allwords=s1.split()+s2.split()
        counts=Counter(allwords)
        return [word for word, count in counts.items() if count==1]