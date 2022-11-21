from collections import deque

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.right = None
        self.left = None
        self.parent = None
    def __str__(self):
        return self.key

def insert_tree(root, node):
    if root is None:
        root = node
    else:
        if root.key > node.key:
            if root.left is None:
                root.left = node
            else:
                insert_tree(root.left, node)
        elif root.key < node.key:
            if root.right is None:
                root.right = node
            else:
                insert_tree(root.right, node)

def sort_max(root):
    if root != None:
        sort_max(root.left)
        print(root.key, end = ' ')
        sort_max(root.right)

def sort_min(root):
    if root != None:
        sort_min(root.right)
        print(root.key, end = ' ')
        sort_min(root.left)

def postorder_traversal(root):
    ans = []
    def helper(node):
        if node != None:
            helper(node.left)
            helper(node.right)
            ans.append(node.key)
    helper(root)
    print(ans)

def Bfs(root):
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

def main():
    tree = Node(8)
    insert_tree(tree, Node(3))
    insert_tree(tree, Node(1))
    insert_tree(tree, Node(6))
    insert_tree(tree, Node(4))
    insert_tree(tree, Node(7))
    insert_tree(tree, Node(10))
    insert_tree(tree, Node(14))
    insert_tree(tree, Node(13))

    sort_max(tree)
    print('\n')

    sort_min(tree)
    print('\n')

    postorder_traversal(tree)
    print('\n')

    Bfs(tree)
    print('\n')

if __name__ == '__main__':
    main()



