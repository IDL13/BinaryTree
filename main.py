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

def sort_min( root):
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
        
def hash_path_sum(root, target_sum):
    def helper(node, total):
        if not node:
            return False
        elif not node.left and not node.ritht:
            if total + node.key == target_sum:
                return True
            else:
                return helper(node.left, total + node.val) or helper(node.right, total + node.val)
    if root:
        return helper(root, 0)
    
def maxDepth(root):
    def dfs(node, currDepth):
        if node is None:
            return currDepth
        else:
            return max(dfs(node.left, currDepth + 1), dfs(node.right, currDepth + 1))
    res = dfs(root, 0)
    print(res)

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




