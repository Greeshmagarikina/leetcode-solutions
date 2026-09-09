class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts={}
        for num in arr:
            counts[num]=counts.get(num,0)+1
        values=list(counts.values())
        uniques=set(values)
        return len(values)==len(uniques)
        