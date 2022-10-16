#Link: https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head==None:
            return None
        if head.val==val:
            return self.removeElements(head.next,val)
        next_el=self.removeElements(head.next,val)
        head.next=next_el
        return head