"""

Problem 25: Reverse Nodes in k-Group

    Given the head of a linked list, reverse the nodes of the list k at a time,
    and return the modified list.

    k is a positive integer and is less than or equal to the length of the
    linked list. If the number of nodes is not a multiple of k then left-out
    nodes, in the end, should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves
    may be changed.

    Example 1:

    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

    Example 2:

    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

    Constraints:

    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000

"""

from typing import Optional

from src.problem_0025.listnode import ListNode


class Solution:
    def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Reverse the nodes of the list k at a time.

        Args:
            head (Optional[ListNode]): The head of the list.
            k (int): The number of nodes to reverse.

        Returns:
            Optional[ListNode]: The head of the list.
        """

        head_: ListNode = ListNode(0, head)
        group_prev: ListNode = head_

        while True:
            kth = self.get_kth(group_prev, k)

            if kth is None:
                break

            group_next: ListNode = kth.next
            prev, current = group_next, group_prev.next

            while current != group_next:
                next_: ListNode = current.next
                current.next = prev
                prev = current
                current = next_

            next_: ListNode = group_prev.next
            group_prev.next = kth
            group_prev = next_

        return head_.next

    def get_kth(self, head: ListNode, k: int) -> ListNode:
        """Get the kth node in the list.

        Args:
            head (ListNode) : The head of the list.
            k (int)         : The index of the node to get.

        Returns:
            ListNode: The kth node.
        """

        while k > 0 and head is not None:
            head = head.next
            k -= 1

        return head

    def reverse_k_group_simple(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        """Reverse the nodes of the list k at a time.

        Args:
            head (Optional[ListNode]): The head of the list.
            k (int): The number of nodes to reverse.

        Returns:
            Optional[ListNode]: The head of the list.
        """

        length: int = self._find_length(head)

        if length < k:
            return head

        current: ListNode = head

        for _ in range(k):
            current = current.next

        current = self.reverse_k_group(current, k)

        for _ in range(k):
            next_: ListNode = head.next
            head.next = current
            current = head
            head = next_

        return current

    def _find_length(self, head: Optional[ListNode]) -> int:
        """Find the length of the list.

        Args:
            head (Optional[ListNode]): The head of the list.

        Returns:
            int: The length of the list.
        """

        length: int = 0

        while head is not None:
            head = head.next
            length += 1

        return length
