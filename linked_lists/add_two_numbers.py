"""
LeetCode 2
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
"""

class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None

def add_tow_numbers(l1, l2):
    l3 = ListNode('*')
    c3 = l3
    carry = 0
    while l1 or l2:
        if l1:
            v1 = l1.val
            l1 = l1.next
        else:
            v1 = 0
        if l2:
            v2 = l2.val
            l2 = l2.next
        else:
            v2 = 0
        cs = v1 + v2 + carry
        v3 = cs % 10
        carry = cs / 10
        c3.next = ListNode(v3)
        c3 = c3.next
    if carry:
        c3.next = ListNode(carry)
    return l3.next

def test_add_two_numbers():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    res = add_tow_numbers(l1, l2)
    assert res.val == 7
    assert res.next.val == 0
    assert res.next.next.val == 8