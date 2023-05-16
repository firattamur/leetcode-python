import pytest

from src.problem_0153.problem_0153 import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_case1(solution: Solution) -> None:
    nums = [3, 4, 5, 1, 2]
    expected = 1

    actual = solution.find_min(nums)

    assert actual == expected


def test_case2(solution: Solution) -> None:
    nums = [4, 5, 6, 7, 0, 1, 2]
    expected = 0

    actual = solution.find_min(nums)

    assert actual == expected


def test_case3(solution: Solution) -> None:
    nums = [11, 13, 15, 17]
    expected = 11

    actual = solution.find_min(nums)

    assert actual == expected
