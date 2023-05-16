import pytest

from src.problem_0121.problem_0121 import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_case1(solution: Solution) -> None:
    prices = [7, 1, 5, 3, 6, 4]
    expected = 5

    actual = solution.max_profit(prices)

    assert actual == expected


def test_case2(solution: Solution) -> None:
    prices = [7, 6, 4, 3, 1]
    expected = 0

    actual = solution.max_profit(prices)

    assert actual == expected


def test_case3(solution: Solution) -> None:
    prices = []
    expected = 0

    actual = solution.max_profit(prices)

    assert actual == expected
