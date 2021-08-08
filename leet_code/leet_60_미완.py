
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        node = head
        next_node = node.next
        while next_node.next:
            node = node.next
            next_node = next_node.next

        return node