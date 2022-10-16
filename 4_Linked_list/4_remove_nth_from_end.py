#Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return head
        p1=head
        p2=head
        prevp1=None;
        while n:
            p2=p2.next
            n-=1
        while p2:
            prevp1=p1
            p1=p1.next
            p2=p2.next
        #if prevp1 has not changed means it didn't go into while loop or 1st ele to delete
        if prevp1==None:
            return p1.next
        else:
            prevp1.next=p1.next
            
        return head
        