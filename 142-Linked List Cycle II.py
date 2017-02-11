# Description
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Note: Do not modify the linked list.
#
# Follow up:
# Can you solve it without using extra space?

# --------------------------------------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow = head;
        fast = head;
        while fast and fast.next:
            fast = fast.next.next;
            slow = slow.next;
        
            if fast == slow:
                slow2 = head;
                while slow2 is not slow:
                    slow2 = slow2.next;
                    slow = slow.next;
                return slow2
        return None
        