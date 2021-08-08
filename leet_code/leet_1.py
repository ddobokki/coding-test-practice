
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode()
l2 = ListNode()
l3 = ListNode()
l4 = ListNode()
l1.val = 9
l2.val = 8
l3.val = 7
l4.val = 0

l1.next = l2
l2.next = l3
l3.next = l4

if l4:
    print(1)
