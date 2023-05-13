import pytest

from src.problem_0022.problem_0022 import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_case1(solution: Solution) -> None:
    n = 3
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]

    actual = solution.generate_parenthesis(n)

    assert sorted(actual) == sorted(expected)


def test_case2(solution: Solution) -> None:
    n = 1
    expected = ["()"]

    actual = solution.generate_parenthesis(n)

    assert sorted(actual) == sorted(expected)
