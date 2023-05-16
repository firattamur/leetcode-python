"""

Problem 217: Contains Duplicate

    Given an integer array nums, return true if any value appears at least
    twice in the array, and return false if every element is distinct.

    Example 1:

    Input: nums = [1,2,3,1]
    Output: true
    Example 2:

    Input: nums = [1,2,3,4]
    Output: false
    Example 3:

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

"""

from typing import Dict, List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """Return true if any value appears at least twice in the array, and
        return false if every element is distinct.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            bool: True if any value appears at least twice in the array, and
            return false if every element is distinct.
        """

        if len(nums) == 0:
            return False

        hashmap: Dict[int, int] = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]] = 1

        return False
