import pytest

from src.problem_0001.problem_0001 import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_case1(solution: Solution):
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]

    actual = solution.two_sum(nums, target)

    assert actual == expected


def test_case2(solution: Solution):
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]

    actual = solution.two_sum(nums, target)

    assert actual == expected


def test_case3(solution: Solution):
    nums = [3, 3]
    target = 6
    expected = [0, 1]

    actual = solution.two_sum(nums, target)

    assert actual == expected


def test_case4(solution: Solution):
    nums = [3, 2, 3]
    target = 6
    expected = [0, 2]

    actual = solution.two_sum(nums, target)

    assert actual == expected
