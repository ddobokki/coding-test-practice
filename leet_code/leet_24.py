# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head

        while node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        return head