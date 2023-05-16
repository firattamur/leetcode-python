import pytest

from src.problem_0025.listnode import ListNode
from src.problem_0025.problem_0025 import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def list_to_listnode(list_: list[int]) -> ListNode:
    """Convert a list to a ListNode object.

    Args:
        list_ (list[int]): The list to convert.

    Returns:
        ListNode: The head of the list.
    """

    head: ListNode = ListNode()
    current: ListNode = head

    for val in list_:
        current.next = ListNode(val)
        current = current.next

    return head.next


def equals(list1: ListNode, list2: ListNode) -> bool:
    if list1 is None and list2 is None:
        return True

    if list1 is None or list2 is None:
        return False

    if list1.val != list2.val:
        return False

    return equals(list1.next, list2.next)


def test_case1(solution: Solution) -> None:
    head = list_to_listnode([1, 2, 3, 4, 5])
    expected = list_to_listnode([2, 1, 4, 3, 5])

    actual = solution.reverse_k_group(head, 2)

    assert equals(actual, expected)


def test_case2(solution: Solution) -> None:
    head = list_to_listnode([1, 2, 3, 4, 5])
    expected = list_to_listnode([3, 2, 1, 4, 5])

    actual = solution.reverse_k_group(head, 3)

    assert equals(actual, expected)


def test_case3(solution: Solution) -> None:
    head = list_to_listnode([1, 2, 3, 4, 5])
    expected = list_to_listnode([4, 3, 2, 1, 5])

    actual = solution.reverse_k_group(head, 4)

    assert equals(actual, expected)
