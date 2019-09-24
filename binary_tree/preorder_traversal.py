"""
Leetcode 144
Given a binary tree, return the preorder traversal of its nodes' values.
Recursive solution is trivial, could you do it iteratively?
"""

class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

def preorder_iterative(root):
    stack, res = [], []
    curr = root
    while curr or stack:
        if curr:
            res.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)
        curr = stack.pop()
    return res

def preorder_recursive(root):
    res = []
    def helper(node):
        if node:
            res.append(node.val)
            helper(node.left)
            helper(node.right)
    helper(root)
    return res

def test_preorder_iterative():
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')
    G = Node('G')
    H = Node('H')
    I = Node('I')
    F.left = B
    F.right = G
    B.left = A
    B.right = D
    D.left = C
    D.right = E
    G.right = I
    I.left = H
    assert preorder_iterative(F) == ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    assert preorder_recursive(F) == ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']