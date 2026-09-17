# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prevSlow, slow, fast = None, head, head
        count = 1
        while fast:
            fast = fast.next
            if (count > n):
                prevSlow = slow
                slow = slow.next
            count += 1
        
        # remove 
        if prevSlow:
            prevSlow.next = slow.next
            return head
        else:
            return head.next

        
        


        
        