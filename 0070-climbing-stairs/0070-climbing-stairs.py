class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        twostep=1
        onestep=2
        for _ in range(3,n+1):
            current=twostep+onestep
            twostep=onestep
            onestep=current
        return onestep
            