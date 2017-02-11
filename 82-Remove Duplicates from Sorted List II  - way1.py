# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# --------------------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        if head and head.next:
            pre = dummy
            first = head
            second = head.next
            flag = 0
            while second:
                if first.val == second.val:
                    flag = flag + 1
                    if second.next is None:
                        pre.next = None
                        break
                    else:
                        second = second.next
                        first.next = second
                elif flag > 0 and first.val != second.val:
                    pre.next = second
                    first = second
                    if second.next is None:
                        break
                    else:
                        second = second.next
                        flag = 0
                elif flag == 0 and first.val != second.val:
                    pre = pre.next
                    first = first.next
                    if second.next is None:
                        break
                    else:
                        second = second.next
        return dummy.next
        