class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def isListEmpty(self):
        # method to check list content
        if self.head is None:
            return True
        else:
            return False

    def listLen(self):
        # method to find list length
        current_node = self.head
        length = 0
        while current_node.next is not None:
            length += 1
            current_node = current_node.next
        return length

    def insertHead(self, new_node):
        temporaryNode = self.head # assigning original head to a temporary variable
        self.head = new_node # adding our desired head
        self.head.next = temporaryNode # pointing our desired head to the original head
        del temporaryNode # doing away with the temporary variable
    
    def insertAt(self, new_node, position):
        if position < 0 or position > self.listLen():
            print("Invalid choice!")
            return
        if position == 0:
            self.insertHead(new_node)
            return
        current_node = self.head
        current_position = 0
        while True:
            if current_position == position:
                previous_node.next = new_node
                new_node.next = current_node
                break
            previous_node = current_node
            current_node = current_node.next
            current_position += 1

    def insertEnd(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    last_node.next = new_node
                    break
                last_node = last_node.next
    
    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("Linked list is empty! Delete failed.")

    def deleteAt(self, position):
        if position < 0 or position >= self.listLen():
            print("Invalid position!")
            return
        if self.isListEmpty() is False:
            if position == 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                else:
                    previousNode = currentNode
                    currentNode = currentNode.next
                    currentPosition += 1
        else:
            print("Linked list is empty! Delete failed.")

    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def printlist(self):
        if self.head is None:
            print("The list is empty.")
        current_node = self.head
        while True:
            if current_node is None:
                break
            else:
                print(current_node.data)
                current_node = current_node.next


first_node = Node(1)
linked_list = Linkedlist()
linked_list.insertEnd(first_node)
second_node = Node(3)
linked_list.insertEnd(second_node)
third_node = Node(2)
linked_list.insertAt(third_node, 1)
linked_list.deleteAt(0) 

linked_list.printlist()