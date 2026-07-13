class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample="123456789"
        result=[]
        min=len(str(low))
        max=len(str(high))
        for length in range(min,max+1):
            for start in range(10-length):
                sub=sample[start:start+length]
                num=int(sub)
                if low<=num<=high:
                    result.append(num)
        return result