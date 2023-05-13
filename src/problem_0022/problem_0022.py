"""

Problem 22: Generate Parentheses

    Given n pairs of parentheses, write a function to generate all
    combinations of well-formed parentheses.

    Example 1:

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:

    Input: n = 1
    Output: ["()"]

    Constraints:

    1 <= n <= 8

"""

from typing import List


class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:
        """Generate all combinations of well-formed parentheses.

        Args:
            n (int): The number of pairs of parentheses.

        Returns:
            List[str]: The list of all combinations of well-formed parentheses.
        """

        result: List[str] = []
        current: List[str] = []

        self._generate_parenthesis(result, n, 0, 0, current)

        return result

    def _generate_parenthesis(
        self, result: List[str], n: int, open: int, close: int, current: List[str]
    ) -> None:
        """Backtracking helper function.

        Args:
            result (List[str])  : The list of well-formed parentheses.
            n (int)             : The number of pairs of parentheses.
            open (int)          : The number of open parentheses.
            close (int)         : The number of close parentheses.
            current (List[str]) : The current combination of parentheses.

        Returns:
            None: This function does not return anything.
        """
        if open == n and close == n:
            result.append("".join(current))
            return

        if open < n:
            current.append("(")
            self._generate_parenthesis(result, n, open + 1, close, current)
            current.pop()

        if close < open:
            current.append(")")
            self._generate_parenthesis(result, n, open, close + 1, current)
            current.pop()
