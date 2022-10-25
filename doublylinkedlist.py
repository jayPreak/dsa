import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None

    #at front
    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("the prev node is null")
            return
        
        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

        new_node.prev = last

        return

    def deleteNode(self, dele):
        if self.head is None or dele is None:
            return
        
        if self.head == dele:
            self.head = dele.next

        if dele.next is not None:
            dele.next.prev = dele.prev

        if dele.prev is not None:
            dele.prev.next = dele.next

        gc.collect()

    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev

    def printList(self, node):
        print("\n in forward")
        while node:
            print(" {}".format(node.data), end=" ")
            last = node
            node = node.next

        print("\n in backward")
        while last:
            print(" {}".format(last.data), end=" ")
            last = last.prev

if __name__ == "__main__":
    llist = DoublyLinkedList()

    llist.append(6)

    llist.push(7)

    llist.push(1)

    llist.append(4)

    llist.insertAfter(llist.head.next, 8)


    

    print("Created DLL is: ")
    llist.printList(llist.head)

    llist.deleteNode(llist.head)
    llist.deleteNode(llist.head.next)
    # llist.deleteNode(llist.head.next)

    print("\nDll after deletion: ")
    llist.printList(llist.head)

    llist.reverse()
    print("\nDll after reversion😎: ")
    llist.printList(llist.head)


        



