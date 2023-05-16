class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        """Initialize a ListNode object."""
        self.val = val
        self.next = next

    def print(self) -> None:
        """Print the list."""
        current: ListNode = self

        while current is not None:
            print(current.val, end=" -> ")
            current = current.next

        print("None")
