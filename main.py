from collections import deque

class BinaryTree:
    class Node:
        def __init__(self, key) -> None:
            self.key = key
            self.right = None
            self.left = None
            self.parent = None

        def __str__(self):
            return self.key

    def insert_tree(self, root, node):
        if root is None:
            root = node
        else:
            if root.key > node.key:
                if root.left is None:
                    root.left = node
                else:
                    self.insert_tree(root.left, node)
            elif root.key < node.key:
                if root.right is None:
                    root.right = node
                else:
                    self.insert_tree(root.right, node)

    def sort_max(self, root):
        if root != None:
            self.sort_max(root.left)
            print(root.key, end = ' ')
            self.sort_max(root.right)

    def sort_min(self, root):
        if root != None:
            self.sort_min(root.right)
            print(root.key, end = ' ')
            self.sort_min(root.left)

    def postorder_traversal(self, root):
        ans = []
        def helper(node):
            if node != None:
                helper(node.left)
                helper(node.right)
                ans.append(node.key)
        helper(root)
        print(ans)

    def Bfs(sefl, root):
        q = deque([root])
        levels = []
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.key)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            levels.append(level)
        print(levels)
        
binary_tree = BinaryTree
tree = binary_tree.Node(8)
binary_tree.insert_tree(tree, binary_tree.Node(3))
binary_tree.insert_tree(tree, binary_tree.Node(1))
binary_tree.insert_tree(tree, binary_tree.Node(6))
binary_tree.insert_tree(tree, binary_tree.Node(4))
binary_tree.insert_tree(tree, binary_tree.Node(7))
binary_tree.insert_tree(tree, binary_tree.Node(10))
binary_tree.insert_tree(tree, binary_tree.Node(14))
binary_tree.insert_tree(tree, binary_tree.Node(13))

binary_tree.sort_max(tree)
print('\n')

binary_tree.sort_min(tree)
print('\n')

binary_tree.postorder_traversal(tree)
print('\n')

binary_tree.Bfs(tree)
print('\n')




