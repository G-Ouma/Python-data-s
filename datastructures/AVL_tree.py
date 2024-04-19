'''
implememntation of an AVL tree

KEY POINTS:
1) It is a balanced search tree
2) The worst case scenario of a binary tree is a linked list; complexity becomes 0(N)
3) AVL trees solves thos problem!
4) We have to maintain the "height" of each node and its children.
5) The height of any node is the number of layers in the tree; longest path from the parent node to the leaf node.
   "height = max(left child's height, right child's height) + 1", to compensate the None(None = -1)
6) The difference (balance factor) in the height of the left sub-tree and the right sub-tree cannot be more than 1.
7) If the difference is more than 1, we rotate the node to the left or the right, to keep the tree balanced.
8) We have 4 conditions to take care of:
    A) left-left heavy; left child's height - Right child's height > 1, node rotated to the right
    B) left-right heavy; balance factor of node.left is < -1 or 0
    C) right-right heavy; left child's height - right child's height < -1, node rotated to the left
    D) right-left heavy; balance factor of node.righ is > 1 0r 0

    a) LEFT LEFT    b) LEFT RIGHT       c) RIGHT RIGHT           d) RIGHT LEFT
           1                1                   1                        1 
          2               2                       2                        2
        3                   3                       3                    3

           2                 1                   2                       1 
         3   1             3                   1   3                       3
                         2                                                   2

                           3                                             3
                         2    1                                        1   2

'''


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.height = 0
        self.left = None
        self.right = None


class AVL:
    def __init__(self):
        self.__root = None

    def insert(self, data):
        # list is empty, has no root
        if not self.__root:
            self.__root = Node(data) # root node has no parent
        # list has a root   
        else:
            self.__insertData(data, self.__root)

    def __insertData(self, data, node):
        if data < node.data:
            if node.left:
                self.__insertData(data, node.left)
            else:
                node.left = Node(data, node)
                self.__violationHandler(node.left)
        elif data > node.data:
            if node.right:
                self.__insertData(data, node.right)
            else:
                node.right = Node(data, node)
                self.__violationHandler(node.right)
    
    def __violationHandler(self, node):
        while node: # node is not a none
            # setting the height
            node.height = max(self.__calculateHeight(node.left), self.__calculateHeight(node.right)) + 1
            self.__violationFix(node)
            node = node.parent # to traverse up to the root node

    def __calculateHeight(self, node):
        '''height = max(left child's height, right child's height) + 1'''
        if not node:
            return -1
        return node.height
    
    def __violationFix(self, node)
        # left left heavy
        if self.__balanceFactor(node) > 1:
            # left right heavy
            if self.__balanceFactor(node.left) < 0: # -1 gives an infinite loop
                self.__rotateLeft(node.left)
            self.__rotateRight(node)
        # right right heavy
        elif self.__balanceFactor(node) < -1:
            # right left heavy
            if self.__balanceFactor(node.right) > 0: # avoid infinite loop
                self.__rotateRight(node.right)
            self.__rotateLeft(node)

    def __balanceFactor(self, node):
        '''The difference btwn the left child's height and the right child's height'''
        if not node:
            return 0
        return self.__calculateHeight(node.left) - self.__calculateHeight(node.right)
    
    def __rotateLeft(self, node):
        tempRightNode = node.right
        t = node.right.left

        # updating references
        tempRightNode.left = node
        node.right = t

        # update child to parent relationship
        tempParent = node.parent
        tempParent.parent = tempParent
        node.parent = tempRightNode
        if t :
            t.parent = node

        # update parent to child relationship
        if tempRightNode.parent: # it is not a root node
            if tempRightNode.parent.left == node:
                tempRightNode.parent = tempRightNode
            elif tempRightNode.parent.right == node:
                tempRightNode.parent.right = tempRightNode
        # if it is a root node
        else:
            self.__root = tempRightNode

        # update the node height
        node.height = max(self.__calculateHeight(node.left), self.__calculateHeight(node.right)) + 1
        tempRightNode.height = max(self.__calculateHeight(tempRightNode.left), self.__calculateHeight(node.right)) + 1

    def __rotateRight(self, node):
        pass

    def remove(self, data):
        if not self.__root:
            print("List is empty. No data to remove!")
        else:
            self.__removeData(data, self.__root)

    def __removeData(self, data, node):
        try:
            if data < node.data:
                if node.left:
                    self.__removeData(data, node.left)
            elif data > node.data:
                if node.right:
                    self.__removeData(data, node.right)
            elif data == node.data:
                # node has no children
                if not node.left and not node.right:
                    parentNode = node.parent
                    if parentNode:
                        if parentNode.left == node:
                            parentNode.left = None
                        elif parentNode.right == node:
                            parentNode.right = None
                    # if the node is not a root node
                    else:
                        self.__root = None
                    del node
                    self.__violationHandler(parentNode)
                # node has only left child
                elif node.left and not node.right:
                    parentNode = node.parent
                    if parentNode:
                        if parentNode.left == node:
                            parentNode.left = node.left
                        elif parentNode.right == node:
                            parentNode.right = node.left
                        # updating the child parent relationship
                        node.left.parent = parentNode
                    else:
                        self.__root = node.left
                    del node
                    self.__violationHandler(parentNode)
                # node has only right child
                elif node.right and not node.left:
                    parentNode = node.parent
                    if parentNode:
                        if parentNode.left == node:
                            parentNode.left = node.right
                        elif parentNode.right == node:
                            parentNode.right = node.right
                        # updating the child-parent relationship
                        node.right.parent = parentNode
                    else:
                        self.__root = node.right
                    del node
                    self.__violationHandler(parentNode)
                # node has both children
                elif node.left and node.right:
                    # finding the smallest (left-most) value/node in the right branch
                    successorNode = self.__findSuccessor(node.right)
                    # swapping the values/node
                    node.data, predecessorNode.data = predecessorNode.data, node.data
                    # deleting the swapped value
                    self.__removeData(successorNode.data, node.left)
        except(TypeError, ValueError):
            print("Data not found")

    def __findSuccessor(self, node):
        if node.left:
            return self.__findPredecessor(node.left)
        else:
            return node

    def find(self, data):
        if not self.__root:
            print("List is empty. No data to find.")
        else:
            self.__findData(data, self.__root)

    def __findData(self, data, node):
        if data < node.data:
            

    def transverse(self):
        if not self.__root:
            print("List is empty. Please add some data.")
        else:
            return self.__in_order(self.__root)

    def __in_order(self, node): # for pre-order or post-order, the sequence of arrangement is changed
        if node.left:
            self.__in_order(node.left)
        
        print(node.data)
        
        if node.right:
            self.__in_order(node.right)

            

if __name__ == "__main__":
    tree = AVL()
    tree.insert(40)
    tree.insert(34)
    tree.insert(24)
    tree.insert(54)
    tree.insert(14)
    tree.insert(6)
    tree.insert(74)
    tree.insert(13)

    tree.transverse()
    print()

    tree.remove(40)
    tree.remove(54)
    tree.remove(74)

    tree.transverse()