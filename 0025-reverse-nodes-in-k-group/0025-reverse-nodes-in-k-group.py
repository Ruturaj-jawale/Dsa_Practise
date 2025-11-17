# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Find kth node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    # fewer than k nodes remain
                    return dummy.next

            group_next = kth.next  # node after the group
            # Reverse the group [group_prev.next .. kth]
            prev = group_next
            curr = group_prev.next

            # Standard in-place reversal until curr hits group_next
            while curr is not group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # After reversal:
            # prev is the new head of this group (original kth)
            # group_prev.next is the old head (now tail)
            tail = group_prev.next  # old head, now tail
            group_prev.next = prev  # connect previous part to reversed head
            group_prev = tail       # set group_prev for next group

        # unreachable but syntactically okay
        return dummy.next
            