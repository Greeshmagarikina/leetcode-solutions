class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts={}
        for num in nums1:
            counts[num]=counts.get(num,0)+1
        result=[]
        for num in nums2:
            if counts.get(num,0)>0:
                result.append(num)
                counts[num]-=1
        return result