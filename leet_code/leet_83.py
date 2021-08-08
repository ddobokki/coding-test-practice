
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return node

node1 = ListNode(1,ListNode(1,ListNode(2,None)))
# print(node1.val)
# print(node1.next.val)
# print(node1.next.next.val)
Solution().deleteDuplicates(node1)