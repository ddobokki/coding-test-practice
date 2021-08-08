class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1 = []
        arr2 = []

        while l1:
            arr1.append(l1.val)
            l1 = l1.next
        while l2:
            arr2.append(l2.val)
            l2 = l2.next

        arr3 = sorted(arr1 + arr2)

        head = node = ListNode()
        for n in arr3:
            node.next = ListNode(n)
            node = node.next
        return head.next