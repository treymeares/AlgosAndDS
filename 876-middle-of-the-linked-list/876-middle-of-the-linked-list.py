# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = [head]
        while res[-1].next:
            res.append(res[-1].next)
        return res[len(res) // 2]
        