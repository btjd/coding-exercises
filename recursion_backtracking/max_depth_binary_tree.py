"""
Leetcode 104
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along 
the longest path from the root node down to the 
farthest leaf node.
"""

class TreeNode(object):
    def __init__(self, v):
        self.value = v
        self.right = None
        self.left = None

def max_depth_binary_tree(root):
    def helper(node, cd, md):
        if node:
            helper(node.left, cd + 1, md)
            helper(node.right, cd + 1, md)
            if cd > md[0]:
                md[0] = cd
        return md[0]
    md = [0]
    return helper(root, 1, md)

def test_max_depth():
    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)
    three.left = nine
    three.right = twenty
    twenty.left = fifteen
    twenty.right = seven

    assert max_depth_binary_tree(three) == 3