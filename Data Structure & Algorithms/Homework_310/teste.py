class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

class Solution:
    def postorderTraversal(self, root):
        stack = [root]
        root = root.left
        result = []
        while stack:
            while root.left != None:
                stack.append(root)
                root = root.left
            
            if root.right != None:
                stack.append(root)
            result.append(root.val)
            root = stack.pop()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

s = Solution()
s.postorderTraversal(root)