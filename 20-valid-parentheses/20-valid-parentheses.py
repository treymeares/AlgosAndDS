class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(","]":"[","}":"{"}
        stack = []
        for c in s:
            if c not in brackets: stack.append(c)
            elif stack:
                top = stack.pop()
                if brackets[c] == top: continue
                else: return False
            else: return False
        return stack == []