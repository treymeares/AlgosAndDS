class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
            # Close bracket
            else:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
        return stack == []