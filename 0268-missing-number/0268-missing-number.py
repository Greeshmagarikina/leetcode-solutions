class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num=0
        for i in range(len(nums)+1):
            num^=i
        for n in nums:
            num^=n
        return num