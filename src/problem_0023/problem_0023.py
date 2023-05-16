"""

Problem 23: Merge k Sorted Lists

    You are given an array of k linked-lists lists,
    each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.

    Example 1:

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6
    Example 2:

    Input: lists = []
    Output: []
    Example 3:

    Input: lists = [[]]
    Output: []

    Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.

"""

from typing import List, Optional

from src.problem_0023.listnode import ListNode


class Solution:
    def merge_k_lists(self, lists: List[ListNode]) -> Optional[ListNode]:
        """Merge k sorted linked lists.

        Args:
            lists (List[ListNode]): The list of linked lists.

        Returns:
            Optional[ListNode]: The head of the merged list.
        """

        if not lists:
            return None

        merged: ListNode = lists[0]

        for i in range(1, len(lists)):
            merged = self._merge_two_lists(merged, lists[i])

        return merged

    def _merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two sorted linked lists.

        Args:
            l1 (ListNode): The head of the first list.
            l2 (ListNode): The head of the second list.

        Returns:
            ListNode: The head of the merged list.
        """

        head: ListNode = ListNode()
        current: ListNode = head

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next

            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if not l1:
            current.next = l2
        else:
            current.next = l1

        return head.next
