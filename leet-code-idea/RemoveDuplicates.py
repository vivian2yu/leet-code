__author__ = 'vivian'
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        self

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

if __name__ == '__main__' :
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    Solution().deleteDuplicates(node1)