class Solution:
    def reverseByType(self, s: str) -> str:
        char=list(s)
        charleft=0
        charright=len(s)-1
        while charleft<charright:
            if not char[charleft].islower():
                charleft+=1
            elif not char[charright].islower():
                charright-=1
            else:
                char[charleft],char[charright]=char[charright],char[charleft]
                charleft+=1
                charright-=1
        spleft=0
        spright=len(s)-1
        while spleft<spright:
            if char[spleft].islower():
                spleft+=1
            elif char[spright].islower():
                spright-=1
            else:
                char[spleft],char[spright]=char[spright],char[spleft]
                spleft+=1
                spright-=1
        return "".join(char)
