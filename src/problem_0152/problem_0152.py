"""

Problem 152: Maximum Product Subarray

    Given an integer array nums, find a
    subarray
    that has the largest product, and return the product.

    The test cases are generated so that the answer will
    fit in a 32-bit integer.

    Example 1:

    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
    Example 2:

    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

    Constraints:

    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10

"""

from typing import List


class Solution:
    def max_product(self, nums: List[int]) -> int:
        """Given an integer array nums, find a subarray that has the largest

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The largest product of a subarray.
        """

        if len(nums) == 0:
            return 0

        result: int = nums[0]
        max_product: int = nums[0]
        min_product: int = nums[0]

        for i in range(1, len(nums)):
            temp: int = max_product

            max_product = max(nums[i], max_product * nums[i], min_product * nums[i])
            min_product = min(nums[i], temp * nums[i], min_product * nums[i])

            result = max(result, max_product)

        return result
