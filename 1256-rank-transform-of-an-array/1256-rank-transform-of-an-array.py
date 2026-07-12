class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sort=sorted(list(set(arr)))
        map={}
        for index, num in enumerate(sort):
            map[num]=index+1
        return [map[num] for num in arr]