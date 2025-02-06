# # Python program for traversal of a linked list
# # Node class


# class Node:

# 	# Function to initialise the node object
# 	def __init__(self, data):
# 		self.data = data # Assign data
# 		self.next = None # Initialize next as null


# # Linked List class contains a Node object
# class LinkedList:

# 	# Function to initialize head
#     def __init__(self):
#         self.head = None

# 	# This function prints contents of linked list
# 	# starting from head
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data)
#             temp = temp.next

#     def getCount(self):
#         temp = self.head  # Initialise temp
#         count = 0  # Initialise count
 
#         # Loop while end of linked list is not reached
#         while (temp):
#             count += 1
#             temp = temp.next
#         return count

#     def push(self, newdata):
#         newnode = Node(newdata)

#         newnode.next = self.head
#         self.head = newnode


# # Code execution starts here
# if __name__ == '__main__':

# 	# Start with the empty list
#     llist = LinkedList()

#     llist.head = Node(1)
#     second = Node(2)
#     third = Node(4)
    
#     llist.head.next = second # Link first node with second
#     second.next = third # Link second node with the third node

#     lisy = LinkedList()

#     lisy.head = Node(1)
#     sec = Node(3)
#     thid = Node(8)

#     lisy.head.next = sec
#     sec.next = thid

#     print("List 1: ")
#     llist.printList()

#     print()

#     print("List2: ")
#     lisy.printList()

#     result = LinkedList()
    
#     result.head = None

#     i = llist.head
#     j = lisy.head
#     while i is not None and j is not None:
#         if i.data < j.data:
#             result.push(i.data)
#             # result.push(j.data)
#             i = i.next
#         elif j.data < i.data:
#             result.push(j.data)
#             # result.push(i.data)
#             j = j.next
#         else:
#             result.push(i.data)
#             result.push(j.data)
#             i = i.next
#             j = j.next

#     if i is not None:
#         result.push(i.data)
    
#     if j is not None:
#         result.push(j.data)
            
        


#     print("restul :")
#     result.printList()        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = dum = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dum.next = list1
                list1 = list1.next
            else:
                dum.next = list2
                list2 = list2.next
            dum = dum.next
                
        if list1:
            dum.next = list1
        if list2:
            dum.next = list2
            
        return result.next
        

