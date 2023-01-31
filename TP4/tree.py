#coding = utf8
"""this program allows you to build a tree with several nodes"""

class BinaryTree():
    """Class to start the root of the tree"""
    def __init__(self):
        self.root=None

class Node():
    """class to be able to add nodes to the roots of the tree"""
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.depth = 0
        self.nodes = []

    def add(self, left = None, right = None):
        """function that add the nodes to the tree"""
        self.left = left
        self.right = right
        if self.left:
            left.depth = self.depth + 1
            left.update_children_depth()
        if self.right:
            right.depth = self.depth + 1
            right.update_children_depth()

    def update_children_depth(self):
        """function that update the children's dept based on the addition
        on the nodes at any point"""
        if self.left:
            self.left.depth = self.depth + 1
            self.left.update_children_depth()
        if self.right:
            self.right.depth = self.depth + 1
            self.right.update_children_depth()

    def display_node(self, level = 0):
        """function that allows you to display the nodes"""
        retour = str(self)
        if self.right:
            retour += "\n"
            for _ in range(0, level+1):
                retour += "\t"
            retour += "right node: " + self.right.display_node(level+1)
        if self.left:
            retour += "\n"
            for _ in range(0, level+1):
                retour += "\t"
            retour += "left node: " + self.left.display_node(level+1)
        return retour

    def __str__(self):
        return str(self.value) + "/" + str(self.depth)

    def is_leaf(self):
        """return self.left == None and self.right == None"""
        return not(self.left or self.right)

    def get_max_depth(self,max_depth=0):
        """Getting the depth of the tree"""
        if self.is_leaf():
            if self.depth > max_depth:
                return self.depth
            else:
                return max_depth
        # je suis le node d'un arbre
        else:
            if self.right:
                max_depth = self.right.get_max_depth(max_depth)

            if self.left:
                max_depth = self.left.get_max_depth(max_depth)
            return max_depth


if __name__ == "__main__":
    node1 = Node(0)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node3.add(node4)
    node1.add(node2, node3)
    tree1=BinaryTree()
    tree1.root=node1

    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node5.add(node6, node7)
    node4.add(node5)
    node8 = Node(8)
    node7.add(node8)

    # print(str(node1.get_max_depth(0)))
    print(node1.display_node())
