class Solution:
    def defangIPaddr(self, address: str) -> str:
        new=[]
        for char in address:
            if char==".":
                new.append("[.]")
            else:
                new.append(char)
        return "".join(new)