# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB
        while one != two:
            one = headB if one is None else one.next
            # print("yes one: ",one)
            two = headA if two is None else two.next
            # print("yes two: ",two)
        return one