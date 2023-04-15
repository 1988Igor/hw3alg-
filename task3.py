# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def print_tree(root):
#     if root:
#         print_tree(root.left)
#         print(root.data)
#         print_tree(root.right)


# def search(root, val):
#     if root is None or root.data == val:
#         return root
#     if root.data > val:
#         return search(root.left, val)
#     else:
#         return search(root.right, val)

# root = Node(10)
# root.left = Node(5)
# root.right = Node(15)
# root.left.left = Node(3)
# root.left.right = Node(8)
# root.right.left = Node(12)
# root.right.right = Node(20)

# print_tree(root)

# node = search(root, 8)
# if node:
#     print(True)
# else:
#     print(False)



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = "RED"

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        self.root = self.insert_helper(self.root, new_node)
        self.root.color = "BLACK"

    def insert_helper(self, current, new_node):
        if not current:
            return new_node
        if new_node.data < current.data:
            current.left = self.insert_helper(current.left, new_node)
        else:
            current.right = self.insert_helper(current.right, new_node)
        if self.is_red(current.right) and not self.is_red(current.left):
            current = self.rotate_left(current)
        if self.is_red(current.left) and self.is_red(current.left.left):
            current = self.rotate_right(current)
        if self.is_red(current.left) and self.is_red(current.right):
            self.flip_colors(current)
        return current

    def search(self, val):
        return self.search_helper(self.root, val)

    def search_helper(self, current, val):
        if not current or current.data == val:
            return current
        if current.data > val:
            return self.search_helper(current.left, val)
        else:
            return self.search_helper(current.right, val)

    def is_red(self, node):
        if not node:
            return False
        return node.color == "RED"

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = "RED"
        return x

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = "RED"
        return x

    def flip_colors(self, node):
        node.color = "RED"
        node.left.color = "BLACK"
        node.right.color = "BLACK"

    def print_tree(self):
        self.print_helper(self.root)

    def print_helper(self, current):
        if current:
            self.print_helper(current.left)
            print(current.data, current.color)
            self.print_helper(current.right)

rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(5)
rb_tree.insert(15)
rb_tree.insert(3)
rb_tree.insert(8)
rb_tree.insert(12)
rb_tree.insert(20)

rb_tree.print_tree()


node = rb_tree.search(8)
if node:
    print(True)
else:
    print(False)


rb_tree.insert(7)
rb_tree.print_tree()
