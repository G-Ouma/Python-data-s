class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def prepend(self, data):
        newNode = Node(data)
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = newNode
            self.__tail = newNode
        else:
            newNode.next = self.__head
            self.__head.prev = newNode
            self.__head = newNode
        self.__size += 1

    def append(self, data):
        newNode = Node(data)
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            newNode.prev = self.__tail
            self.__tail = newNode 
        self.__size += 1

    def addBefore(self, key, data):
        if self.__size == 0 and not self.__head and not self.__tail:
            print("List is empty!")
        else:
            newNode = Node(data)
            currentNode = self.__head
            prevNode = None
            while currentNode:
                if currentNode.data == key:
                    if not prevNode:
                        self.prepend(data)
                    else:
                        prevNode.next = newNode
                        newNode.next = currentNode
                        currentNode.prev = newNode
                        self.__size += 1
                    return
                else:
                    prevNode = currentNode
                    nextNode = currentNode.next
                    currentNode = nextNode
    
    def addAfter(self, key, data):
        if self.__size == 0 and not self.__head and not self.__tail:
            print("List is empty!")
        else:
            newNode = Node(data)
            currentNode = self.__head
            while currentNode:
                if currentNode.data == key:
                    if not currentNode.next:
                        self.append(data)
                    else:
                        nextNode = currentNode.next
                        currentNode.next = newNode
                        newNode.prev = currentNode
                        newNode.next = nextNode
                        nextNode.prev = newNode
                        self.__size += 1
                    return
                else:
                    currentNode = currentNode.next

    def delData(self, data):
        if self.__size == 0 and not self.__head and not self.__tail:
            print("List is empty. No data to remove!")
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
            self.__size -= 1
        elif self.__size > 1:
            currentNode = self.__head
            prevNode = None
            while currentNode:
                if currentNode.data == data:
                    if not prevNode:
                        nextNode = currentNode.next
                        nextNode.prev = None
                        self.__head = nextNode
                        del currentNode
                    elif currentNode.next == None:
                        prevNode = currentNode.prev
                        prevNode.next = None
                        self.__tail = prevNode
                        del currentNode
                    else:
                        nextNode = currentNode.next
                        prevNode.next = nextNode
                        nextNode.prev = prevNode
                        del currentNode
                    return
                else:
                    prevNode = currentNode
                    currentNode = currentNode.next            

    def traverseFWD(self):
        currentNode = self.__head
        if currentNode.data is None:
            print("The List is empty")
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next
        
    def traverseBWD(self):
        currentNode = self.__tail
        if currentNode.data is None:
            print("The List is empty")
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.prev

    def listSize(self):
        if self.__size == 0:
            print("List is empty")
        else:
            return self.__size
        

if __name__ == "__main__":
    doubleList = DoubleList()
    doubleList.append("My")
    doubleList.append("name")
    doubleList.append("Gerald")
    
    doubleList.addBefore("My", "is")
    doubleList.addAfter("name", "Ouma")
    
    doubleList.traverseFWD()
    print()
    print("Size:",doubleList.listSize())
    print()
    doubleList.delData("Gerald")
    doubleList.traverseFWD()

