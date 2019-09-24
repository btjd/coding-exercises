"""
Leetcode 234
Given a singly linked list, determine if it is a palindrome.
"""
class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None

def is_palindrome(head):
    # Find mid poing using fast and slow pointers
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Use the reverse linked list also to 
    # reverse the second half
    p = n = None
    while slow:
        n = slow.next
        slow.next = p
        p = slow
        slow = n
    # Traverse starting from both ends towards
    # the middle and check values are equal
    while p and head:
        if head.val != p.val:
            return False
        else:
            head = head.next
            p = p.next
    return True

def test_is_palindrome():
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    dos = ListNode(2)
    uno = ListNode(1)
    head = one
    one.next = two
    two.next = three
    three.next = dos
    dos.next = uno
    assert is_palindrome(head) is True