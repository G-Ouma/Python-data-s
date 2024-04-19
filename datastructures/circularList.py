class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def prepend(self, data):
        '''Add node in the beginning of the list'''
        newNode = Node(data)
        # Check if list is empty
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = newNode
            self.__tail = newNode
            self.__tail.next = self.__head
            self.__head.prev = self.__tail
        else:
            self.__tail.next = newNode
            newNode.next = self.__head
            self.__head.prev = newNode
            newNode.prev = self.__tail
            self.__head = newNode
        self.__size += 1

    def append(self, data):
        '''Add node at the end of the list'''
        newNode = Node(data)
        # Check if list is empty
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = newNode
            self.__tail = newNode
            self.__tail.next = self.__head
            self.__head.prev = self.__tail
        else:
            self.__tail.next = newNode
            newNode.next = self.__head
            self.__head.prev = newNode
            newNode.prev = self.__tail
            self.__tail = newNode
        self.__size += 1

    def addBefore(self, key, data):
        newNode = Node(data)
        if self.__size == 0 and not self.__head and not self.__tail:
            print("List is empty. Add data to your list.")
        else:
            currentNode = self.__head
            prevNode = None
            while currentNode:
                if currentNode.data == key:
                    if currentNode == self.__head:
                        self.prepend(data)
                    else:
                        currentNode.prev = newNode
                        prevNode.next = newNode
                        newNode.prev = prevNode
                        newNode.next = currentNode
                        self.__size += 1
                    return
                else:
                    prevNode = currentNode
                    currentNode = currentNode.next
                    # Exception for an invalid Key
                    if currentNode == self.__head:
                        print("Requested Key not found in list")
                        break

    def addAfter(self, key, data):
        newNode = Node(data)
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = newNode
            self.__tail = newNode
            self.__tail.next = self.__head
            self.__head.prev = self.__tail
        else:
            currentNode = self.__head
            while currentNode:
                if currentNode.data == key:
                    if currentNode == self.__tail:
                        self.append(data)
                    else:
                        nextNode = currentNode.next
                        nextNode.prev = newNode
                        currentNode.next = newNode
                        newNode.prev = currentNode
                        newNode.next = nextNode
                        self.__size += 1
                    return
                else:
                    currentNode = currentNode.next
                    # Exception for an invalid Key
                    if currentNode == self.__head:
                        print("Requested Key not found in list")
                        break

    def delData(self, data):
        # empty list
        if self.__size == 0 and not self.__head and not self.__tail:
            print("List is empty. No data to remove.")
        # list with one node
        elif self.__size == 1:
            self.__head.prev = None
            self.__tail.next = None
            self.__tail = None
            self.__tail = None
            self.__size -= 1
        # list with more than one node
        elif self.__size > 1:
            currentNode = self.__head
            prevNode = None
            while currentNode:
                if currentNode.data == data:
                    # deleting head node
                    if currentNode == self.__head:
                        nextNode = currentNode.next
                        currentNode.next = None
                        currentNode.prev = None
                        del currentNode
                        nextNode.prev = self.__tail
                        self.__tail.next = nextNode
                        self.__head = nextNode
                    # deleting tail node
                    elif currentNode == self.__tail:
                        currentNode.next = None
                        currentNode.prev = None
                        del currentNode
                        prevNode.next = self.__head
                        self.__head.prev = prevNode
                        self.__tail = prevNode
                    # deleting a random node that is not the tail or head
                    else:
                        nextNode = currentNode.next
                        currentNode.next = None
                        currentNode.prev = None
                        del currentNode
                        prevNode.next = nextNode
                        nextNode.prev = prevNode
                    self.__size -= 1
                    return
                else:
                    prevNode = currentNode
                    currentNode = currentNode.next
                    # Exception for an invalid Key
                    if currentNode == self.__head:
                        print("Requested Key not found in list")
                        break

    def traverseFWD(self):
        # Head to tail list traversal
        if self.__size == 0 and not self.__head and not self.__tail:
            print("The list is empty.")
        else:
            currentNode = self.__head
            while currentNode:
                print(currentNode.data)
                currentNode = currentNode.next
                if currentNode == self.__head:
                    break

    def traverseBWD(self):
        # Tail to head list traversal
        if self.__size == 0 and not self.__head and not self.__tail:
            print("The list is empty.")
        else:
            currentNode = self.__tail
            while currentNode:
                print(currentNode.data)
                currentNode = currentNode.prev
                if currentNode == self.__tail:
                    break

    def listSize(self):
        return self.__size
    

if __name__ == '__main__':
    myList = CircularList()

    myList.append(1)
    myList.append(2)
    myList.append(3)
    myList.prepend(0)

    myList.addAfter(1, 1.5)
    myList.addBefore(0, -0.5)

    # myList.delData(-0.5)

    myList.traverseFWD()
    print()
    myList.traverseBWD()
    print()
    print("Size:", myList.listSize())
