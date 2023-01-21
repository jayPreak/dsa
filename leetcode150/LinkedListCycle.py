# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        while head:
            if head in visited:
                return True
            else:
                visited[head] = True
            head = head.next
        return False


## Another solution

 # Approch 3 single pointer, marking nodes as visited, makes use of fact that node value's are not None
  # Time -O(n), Space- O(1)
slow = head
while(slow):
	if slow.val == None:
		# This was already visited
		return True
	slow.val = None # a way to mark visited
	slow = slow.next
return False