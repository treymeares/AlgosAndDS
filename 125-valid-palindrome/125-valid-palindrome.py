class Solution:
    def isPalindrome(self, s: str) -> bool:
        comp ="".join(letter.lower() for letter in s if letter.isalnum())
        return comp == comp[::-1]