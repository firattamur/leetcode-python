import pytest

from src.problem_0238.problem_0238 import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_case1(solution: Solution) -> None:
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]

    actual = solution.product_except_self(nums)

    assert actual == expected


def test_case2(solution: Solution) -> None:
    nums = [-1, 1, 0, -3, 3]
    expected = [0, 0, 9, 0, 0]

    actual = solution.product_except_self(nums)

    assert actual == expected


def test_case3(solution: Solution) -> None:
    nums = [0, 0]
    expected = [0, 0]

    actual = solution.product_except_self(nums)

    assert actual == expected
