# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        dummyHead.next = head
        prev = dummyHead
        for i in range(n+1):
            curr = curr.next
        while curr:
            curr = curr.next
            prev = prev.next
        prev.next = prev.next.next
        return dummyHead.next
        