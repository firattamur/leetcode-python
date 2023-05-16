import pytest

from src.problem_0027.problem_0027 import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_case1(solution: Solution) -> None:
    nums = [3, 2, 2, 3]
    val = 3
    expected = 2

    actual = solution.remove_element(nums, val)

    assert actual == expected


def test_case2(solution: Solution) -> None:
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    expected = 5

    actual = solution.remove_element(nums, val)

    assert actual == expected


def test_case3(solution: Solution) -> None:
    nums = []
    val = 2
    expected = 0

    actual = solution.remove_element(nums, val)

    assert actual == expected
