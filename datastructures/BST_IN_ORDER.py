"""
Implementing a Binary search Tree

    1) A data structure in which the data is arranged like a tree, 
       also inspired from the concept of binary search

    2) In a tree, there is a root node at the top, 
       through which we can access the DS

    3) each node can have atmost 2 children

    4) The left child is always smaller than its parent node, 
       and the right is always greater than the parent node

    5) Traversing through the tree has 3 ways:
       In-order, Pre-order, Post-order

    6) In-order: - left child -> parent -> right child

    7) Implemented through recursion

    8) Recursion, in short, uses STACK Memory (LIFO)

    9) Time complexity - 0(logN); best case scenario
"""
class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.__root = None # '__' strongly private method/variable

    def insert(self, data):
        # no root node
        if not self.__root:
            self.__root = Node(data)
        # presence of root 
        else:
            self.__insertData(data, self.__root)

    def __insertData(self, data, node):
        # check data
        if data < node.data:
            if node.left:
                # if there is a left node, method calls itself recursively
                self.__insertData(data, node.left)
            else:
                node.left = Node(data, node) # node is the parent node
        elif data > node.data:
            if node.right:
                # if there is a right node, method calls itself recursively
                self.__insertData(data, node.right)
            else:
                node.right = Node(data, node) # node is the parent node

    def remove(self, data):
        if not self.__root:
            print("No data to remove.")
        else:
            self.__removeData(data, self.__root)

    def __removeData(self, data, node):
        try:        
            if data < node.data:
                self.__removeData(data, node.left)
            elif data > node.data:
                self.__removeData(data, node.right)        
            elif data == node.data:
                # i) node has no child
                if not node.left and not node.right:
                    parentNode = node.parent
                    if parentNode:
                        if parentNode.left == node:
                            parentNode.left = None
                        elif parentNode.right == node:
                            parentNode.right = None
                    else:
                        self.__root = None
                    del node
                # ii) node has left child only
                elif node.left and not node.right:
                    parentNode = node.parent
                    if parentNode:
                        if parentNode.left == node:
                            parentNode.left = node.left
                        elif parentNode.right == node:
                            parentNode.right = node.left
                        # updating child parent relationship
                        node.left.parent = parentNode
                    else:
                        self.__root = node.left
                # iii) node has right child only
                elif node.right and not node.left:
                    parentNode = node.parent
                    if parentNode:
                        if parentNode.left == node:
                            parentNode.left = node.right
                        elif parentNode.right == node:
                            parentNode.right = node.right
                        # updating child parent relationship 
                        node.right.parent = parentNode
                    else:
                        self.__root = node.right
                # iv) node has both children
                elif node.left and node.right:
                    # finding the largest value/node (right-most) to the left branch of the node we desire to remove
                    predecessorNode = self.__findPredecessor(node.left)
                    # swapping the right-most value/node with the node we want to remove 
                    node.data, predecessorNode.data = predecessorNode.data, node.data
                    # removing the swapped node
                    self.__removeData(predecessorNode.data, node.left)
        except (AttributeError, TypeError):
            print("Data not found.")

    def __findPredecessor(self, node):
        if node.right:
            return self.__findPredecessor(node.right)
        else:
            return node
    
    def traverseTree(self):
        if self.__root:
            self.__inOrder(self.__root)

    def __inOrder(self, node):
        if node.left:
            self.__inOrder(node.left)
        
        print(node.data)

        if node.right:
            self.__inOrder(node.right)


if __name__ == "__main__":

    tree = BST()
    tree.insert(40)
    tree.insert(4)
    tree.insert(10)
    tree.insert(14)
    tree.insert(9)
    tree.insert(6)
    tree.insert(56)
    tree.insert(73)

    tree.traverseTree()
    print()

    tree.remove(40)
    tree.remove(14)
    tree.remove(56)

    tree.traverseTree()