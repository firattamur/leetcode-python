import pytest

from src.problem_0152.problem_0152 import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_case1(solution: Solution) -> None:
    nums = [2, 3, -2, 4]
    expected = 6

    actual = solution.max_product(nums)

    assert actual == expected


def test_case2(solution: Solution) -> None:
    nums = [-2, 0, -1]
    expected = 0

    actual = solution.max_product(nums)

    assert actual == expected


def test_case3(solution: Solution) -> None:
    nums = [-2]
    expected = -2

    actual = solution.max_product(nums)

    assert actual == expected


def test_case4(solution: Solution) -> None:
    nums = [3, -1, 4]
    expected = 4

    actual = solution.max_product(nums)

    assert actual == expected
