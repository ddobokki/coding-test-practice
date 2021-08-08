# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next

        l2_list = []
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next

        num1 = ''.join(map(str, l1_list[::-1]))
        num2 = ''.join(map(str, l2_list[::-1]))
        num3 = int(num1) + int(num2)
        num3 = list(str(num3))
        num3 = list(map(int, num3))
        num3 = num3[::-1]
        temp = []
        for i in range(len(num3)):
            temp.append(ListNode(num3[i]))

        for i in range(len(temp) - 1):
            temp[i].next = temp[i + 1]
        return temp[0]