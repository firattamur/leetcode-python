import pytest

from src.problem_0023.problem_0023 import ListNode, Solution


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
    """Compare two ListNode objects.

    Args:
        list1 (ListNode): The first list.
        list2 (ListNode): The second list.

    Returns:
        bool: True if the lists are equal, False otherwise.
    """

    if list1 is None and list2 is None:
        return True

    if list1 is None or list2 is None:
        return False

    if list1.val != list2.val:
        return False

    return equals(list1.next, list2.next)


def test_case1(solution: Solution) -> None:
    lists = [
        list_to_listnode([1, 4, 5]),
        list_to_listnode([1, 3, 4]),
        list_to_listnode([2, 6]),
    ]
    expected = list_to_listnode([1, 1, 2, 3, 4, 4, 5, 6])

    actual = solution.merge_k_lists(lists)

    assert equals(actual, expected)


def test_case2(solution: Solution) -> None:
    lists = []
    expected = list_to_listnode([])

    actual = solution.merge_k_lists(lists)

    assert equals(actual, expected)


def test_case3(solution: Solution) -> None:
    lists = [
        list_to_listnode([]),
    ]
    expected = list_to_listnode([])

    actual = solution.merge_k_lists(lists)

    assert equals(actual, expected)
