# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        b = []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next

        x = "".join(map(str, a))
        y = "".join(map(str, b))
        n = int("".join(reversed(x)))
        m = int("".join(reversed(y)))

        res = str(n+m)
        res = "".join(reversed(res))
        answer = ListNode(0)
        result = answer
        for i in range(len(res)):
            result.next = ListNode(int(res[i]))
            result = result.next

        return answer.next

        