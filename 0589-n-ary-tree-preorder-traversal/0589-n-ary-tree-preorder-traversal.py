"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if root is None: 
            return
        result.append(root.val)
        for i in root.children:
            self.traverse(i, result)

            


