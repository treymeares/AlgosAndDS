"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        if not root or not root.left:
            return root
    
        root.left.next = root.right
        root.right.next = None if root.next is None else root.next.left
    
        self.connect(root.left)
        self.connect(root.right)
    
        return root