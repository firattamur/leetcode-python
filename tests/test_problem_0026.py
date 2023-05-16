import pytest

from src.problem_0026.problem_0026 import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_case1(solution: Solution) -> None:
    nums = [1, 1, 2]
    expected = 2

    actual = solution.remove_duplicates(nums)

    assert actual == expected


def test_case2(solution: Solution) -> None:
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected = 5

    actual = solution.remove_duplicates(nums)

    assert actual == expected


def test_case3(solution: Solution) -> None:
    nums = []
    expected = 0

    actual = solution.remove_duplicates(nums)

    assert actual == expected
