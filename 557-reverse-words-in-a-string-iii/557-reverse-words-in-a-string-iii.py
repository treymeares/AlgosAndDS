class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        new = s.split()
        print(new)
        return " ".join(new[::-1])
        