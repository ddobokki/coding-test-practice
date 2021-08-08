# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next

        temp.pop(-n)
        head = node = ListNode()
        for t in temp:
            node.next = ListNode(t)
            node = node.next
        return head.next
