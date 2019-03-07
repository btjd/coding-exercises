"""
LeetCode 94
Given a binary tree, return the inorder traversal of its nodes' values
in an iterative (not recursive) manner.
"""

class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder_traversal(root):
    res = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        if stack:
            current = stack.pop()
            res.append(current.val)
            current = current.right
    return res

def test_inorder_traversal():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven
    assert inorder_traversal(one) == [4,2,5,1,6,3,7]