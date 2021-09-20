import binarySearchTree

from node import Node

class testBST:
    def test1(self):
        root = Node(4)
        root.left = Node(2)
        root.right = Node(7)
        root.left.left = Node(1)
        root.left.right = Node(3)

        assert(binarySearchTree.findClosestValueInBST(root, 2) == True)


