class Solution:
    def isValid(self, s: str) -> bool:
        queue,opened = [],{'(':')','[':']','{':'}'}
        for i in s:
            if i in opened:queue.append(i)
            else:
                if not queue or i != opened[queue.pop()]:return False
                
        return not queue