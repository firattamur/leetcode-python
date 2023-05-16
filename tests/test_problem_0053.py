import pytest

from src.problem_0053.problem_0053 import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_case1(solution: Solution) -> None:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6

    actual = solution.max_subarray(nums)

    assert actual == expected


def test_case2(solution: Solution) -> None:
    nums = [1]
    expected = 1

    actual = solution.max_subarray(nums)

    assert actual == expected


def test_case3(solution: Solution) -> None:
    nums = [5, 4, -1, 7, 8]
    expected = 23

    actual = solution.max_subarray(nums)

    assert actual == expected
