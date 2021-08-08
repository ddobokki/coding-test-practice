# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            point = head
            head = head.next
            point.next = prev
            prev = point

        return prev



li = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

Solution().reverseList(li)