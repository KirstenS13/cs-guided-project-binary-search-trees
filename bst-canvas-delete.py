# Construct a binary search tree that can perform basic operations with a logarithmic time complexity

# to create a binary search tree we need two classes:
#   a node class
#   a tree class

# node class
class BSTNode:
    # initialization method
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # insert method
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    
    # search method
    def search(self, target):
        if self.value == target:
            return self
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)

    def delete(self, target):
# PLAN for Delete:
# find the node to delete
    # compare target to current value
        # if target == less than, go left --> set current = left child
        # if target == greater than, go right --> set current = right child
        # repeat until target == current value
        target_node = self.search(target)
        # OR we don't find it
    # if we don't find it, return None
    if target_node is False:
        return False
    # if we do find it: current == target
        # find the replacement
            # go to the left most child on the right subtree
                # while replacement has a left child: replacement = replacement.left
    replacement = self.find_minimum_value()
        # replace the target
            # replacement's parent.left = None
            # target's parent.(left or right)?
                # need to keep track of target's parent
                # and if it's the left or right subchild
            # replacement.left = target.left
            # replacement.right = target.right
    
    def find_minimum_value(self):
        # while current has left child: replacement = replacement.left
        # recursive:
        # base case:
        if self.left is None:
            return self
        return self.left.find_minimum_value()

# tree class
class BST:
    # initialization method
    def __init__(self, value):
        return self.root = BSTNode(value)
    
    # insert method - should be built in to BSTNode as well
    def insert(self, value):
        return self.root.insert(value)

    # search method - should be built in to BSTNode as well
    def search(self, value):
        return self.root.search(value)

    def find_minimum_value(self):
        return self.root.find_minimum_value().value()

bst = BST(38)
