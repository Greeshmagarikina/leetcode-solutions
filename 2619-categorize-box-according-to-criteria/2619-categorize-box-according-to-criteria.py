class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume=length*width*height
        is_Bulky=(length>=10**4 or
                  width>=10**4 or
                  height>=10**4 or
                  mass>=10**4 or 
                  volume>=10**9)
        is_Heavy=mass>=100
        if is_Bulky and is_Heavy:
            return "Both"
        elif not is_Bulky and not is_Heavy:
            return "Neither"
        elif is_Bulky:
            return "Bulky"
        else:
            return "Heavy"
