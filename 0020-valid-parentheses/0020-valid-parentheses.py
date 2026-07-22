class Solution:
    def isValid(self, s: str) -> bool:
        d=[]
        is_valid=True
        for ch in s:
            if ch in '{[(':
                d.append(ch)
            else:
                if len(d)==0:
                    is_valid = False
                    break
                if(ch==']' and d[-1]=='[')or(ch==')' and d[-1]=='(') or (ch=='}' and d[-1]=='{'):
                    d.pop()
                else:
                    is_valid=False
        if len(d)!=0:
            is_valid=False
        return is_valid
        