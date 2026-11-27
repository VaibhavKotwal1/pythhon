from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def insert_level_order(self, value):
        """Inserts a node in the first available spot using breadth-first order."""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.left is None:
                current.left = new_node
                return
            queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            queue.append(current.right)

    def inorder(self, node, result=None):
        """Left -> Root -> Right"""
        if result is None:
            result = []
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)
        return result

    def preorder(self, node, result=None):
        """Root -> Left -> Right"""
        if result is None:
            result = []
        if node:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        return result

    def postorder(self, node, result=None):
        """Left -> Right -> Root"""
        if result is None:
            result = []
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)
        return result


# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    for val in [1, 2, 3, 4, 5, 6]:
        tree.insert_level_order(val)

    print("Inorder:  ", tree.inorder(tree.root))    # [4, 2, 5, 1, 6, 3]
    print("Preorder: ", tree.preorder(tree.root))   # [1, 2, 4, 5, 3, 6]
    print("Postorder:", tree.postorder(tree.root))  # [4, 5, 2, 6, 3, 1]