class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        ans=-1
        while left<=right:
            mid=(left+right)//2
            sqrt=mid*mid
            if sqrt==x:
                return mid
            elif sqrt>x:
                right=mid-1
            else:
                ans=mid
                left=mid+1
        return ans