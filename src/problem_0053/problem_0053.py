"""

Problem 53: Maximum Subarray

    Given an integer array nums, find the
    subarray
    with the largest sum, and return its sum.

    Example 1:

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.
    Example 2:

    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.
    Example 3:

    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

    Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

    Follow up: If you have figured out the O(n) solution, try coding another
    solution using the divide and conquer approach, which is more subtle.

"""

from typing import List


class Solution:
    def max_subarray(self, nums: List[int]) -> int:
        """Given an integer array nums, find the subarray with the largest sum,
        and return its sum.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The sum of the subarray with the largest sum.
        """

        if len(nums) == 0:
            return 0

        result: int = nums[0]
        subarray_sum: int = 0

        for i in range(len(nums)):
            if subarray_sum < 0:
                subarray_sum = 0

            subarray_sum += nums[i]
            result = max(result, subarray_sum)

        return result
