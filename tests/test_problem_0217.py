import pytest

from src.problem_0217.problem_0217 import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_case1(solution: Solution) -> None:
    nums = [1, 2, 3, 1]
    expected = True

    actual = solution.contains_duplicate(nums)

    assert actual == expected


def test_case2(solution: Solution) -> None:
    nums = [1, 2, 3, 4]
    expected = False

    actual = solution.contains_duplicate(nums)

    assert actual == expected


def test_case3(solution: Solution) -> None:
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    expected = True

    actual = solution.contains_duplicate(nums)

    assert actual == expected
