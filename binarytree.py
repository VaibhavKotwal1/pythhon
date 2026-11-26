from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class BinaryTree:
    def __init__(self, root_value: Optional[int] = None):
        self.root: Optional[Node] = Node(root_value) if root_value is not None else None

    def preorder(self) -> List[int]:
        """Root -> Left -> Right"""
        result: List[int] = []

        def _traverse(node: Optional[Node]) -> None:
            if node is None:
                return
            result.append(node.value)
            _traverse(node.left)
            _traverse(node.right)

        _traverse(self.root)
        return result

    def inorder(self) -> List[int]:
        """Left -> Root -> Right"""
        result: List[int] = []

        def _traverse(node: Optional[Node]) -> None:
            if node is None:
                return
            _traverse(node.left)
            result.append(node.value)
            _traverse(node.right)

        _traverse(self.root)
        return result

    def postorder(self) -> List[int]:
        """Left -> Right -> Root"""
        result: List[int] = []

        def _traverse(node: Optional[Node]) -> None:
            if node is None:
                return
            _traverse(node.left)
            _traverse(node.right)
            result.append(node.value)

        _traverse(self.root)
        return result

    def level_order(self) -> List[List[int]]:
        """Breadth-First Search (level by level)"""
        if self.root is None:
            return []

        levels: List[List[int]] = []
        queue: deque[Node] = deque([self.root])

        while queue:
            level_size = len(queue)
            current_level: List[int] = []
            for _ in range(level_size):
                curr = queue.popleft()
                current_level.append(curr.value)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            levels.append(current_level)

        return levels

    def height(self) -> int:
        """Number of edges on the longest path from root to a leaf (-1 if empty)."""
        def _height(node: Optional[Node]) -> int:
            if node is None:
                return -1
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)


# Example usage:
#       1
#      / \
#     2   3
#    / \
#   4   5
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Preorder:", tree.preorder())       # [1, 2, 4, 5, 3]
print("Inorder:", tree.inorder())         # [4, 2, 5, 1, 3]
print("Postorder:", tree.postorder())     # [4, 5, 2, 3, 1]
print("Level-order:", tree.level_order()) # [[1], [2, 3], [4, 5]]
print("Height:", tree.height())           # 2