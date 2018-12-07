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
        Node = set()
        while(head):
            if head in Node:
                return head
            Node.add(head)
            head = head.next
        else:
            return head
