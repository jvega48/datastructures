"""Easy - Coding Challenges - Fast and Slow Pointers"""


# Given the head of a Singly LinkedList, write a function to
# determine if the LinkedList has a cycle in it or not.
class Node:
    """Node Class"""

    def __init__(self, value, next_pointer=None):
        self.value = value
        self.next_pointer = next_pointer


def test_cycle(head):
    """Find if the LinkedList has a cycle"""
    if head is None:
        return False
    slow = fast = head

    while fast is not None and fast.next_pointer is not None:
        slow = slow.next_pointer
        fast = fast.next_pointer.next_pointer
        if slow == fast:
            return True

    return False


def middle_of_linked_list(head):
    """Find if the middle of the LinkedList"""
    if head is None:
        return None
    slow = fast = None
    while fast is not None and fast.next_pointer is not None:
        slow = slow.next_pointer
        fast = fast.next_pointer.next_pointer

    return slow


def middle_of_linked_list_2(head):
    """Find if the middle of the LinkedList"""
    if head is None:
        return None
    slow = fast = head

    size_of_list = 1

    while fast is not None and fast.next_pointer is not None:
        slow = slow.next_pointer
        fast = fast.next_pointer.next_pointer

        size_of_list += 2

        if size_of_list % 2 == 0:
            return slow.next
    return slow
