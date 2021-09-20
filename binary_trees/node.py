class Node:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if node.left:
                self.insertNode(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insertNode(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        if self.root:
            return self.findNode(data, self.root)
        else:
            return None

    def findNode(self, data, node):
        if data == node.data:
            return node
        elif data < node.data:
            if node.left:
                self.findNode(data, node.left)
            else:
                return None
        else:
            if node.right:
                self.findNode(data, node.right)
            else:
                return None

    def delete(self, data):
        if self.root:
            self.deleteNode(data, self.root)

    def deleteNode(self, data, node):
        if data < node.data:
            if node.left:
                self.deleteNode(data, node.left)
        elif data > node.data:
            if node.right:
                self.deleteNode(data, node.right)
        else:
            if node.left is None and node.right is None:
                del node
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                tempNode = node.right
                while tempNode.left:
                    tempNode = tempNode.left
                node.data = tempNode.data
                self.deleteNode(tempNode.data, node.right)