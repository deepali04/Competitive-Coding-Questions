class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        length=len(s)        
        mid=length//2
        first=s[0:mid]
        second=s[mid:length]
        vowelcountfirst=vowelcountsecond=0
        for i in first:
            if i in ['a','e','i','o','u']:
                vowelcountfirst+=1
        for i in second:
            if i in ['a','e','i','o','u']:
                vowelcountsecond+=1
        if vowelcountsecond==vowelcountfirst:
            return True
        return False
        
        