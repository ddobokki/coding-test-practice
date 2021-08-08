Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        return_node = before_node = ListNode(0,head)

        while head:

            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                before_node.next = head.next
            else:
                before_node = before_node.next

            head = head.next
        return return_node.next