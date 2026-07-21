class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            current=0
            while n>0:
                digit=n%10
                current+=digit**2
                n=n//10
            n=current
        return n==1