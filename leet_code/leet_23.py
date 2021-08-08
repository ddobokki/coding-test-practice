from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        all_list = []
        for al in lists:
            temp = []
            while al:
                temp.append(al.val)
                al = al.next
            all_list.append(temp)
        a = []
        for al in all_list:
            a += al
        a.sort()
        head = node = ListNode()
        for n in a:
            node.next = ListNode(n)
            node = node.next
        return head.next
