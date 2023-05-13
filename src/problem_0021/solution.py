"""

Problem 21: Amicable numbers

    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list.
    The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    Example 1:

    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    Example 2:

    Input: list1 = [], list2 = []
    Output: []
    Example 3:

    Input: list1 = [], list2 = [0]
    Output: [0]

    Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

"""

from typing import Optional

from src.problem_0021.listnode import ListNode


class Solution:
    def merge_two_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Merge two sorted linked lists.

        Args:
            list1 (Optional[ListNode]): The head of the first list.
            list2 (Optional[ListNode]): The head of the second list.

        Returns:
            Optional[ListNode]: The head of the merged list.
        """

        l1head: ListNode = list1
        l2head: ListNode = list2

        merged: ListNode = ListNode()

        if l1head is None and l2head is None:
            return None

        if l1head is None:
            return l2head

        if l2head is None:
            return l1head

        if l1head.val <= l2head.val:
            merged.val = l1head.val
            l1head = l1head.next

        else:
            merged.val = l2head.val
            l2head = l2head.next

        merged.next = self.merge_two_lists(l1head, l2head)

        return merged
