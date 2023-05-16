"""

Problem 238: Product of Array Except Self

    Given an integer array nums, return an array answer such that answer[i] is
    equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit
    in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the
    division operation.

    Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

    Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30

    The product of any prefix or suffix of nums is guaranteed to fit
    in a 32-bit integer.


"""

from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        """Product of all the elements of nums except nums[i].

        Args:
            nums (List[int]): The list of integers.

        Returns:
            List[int]: The product of all the elements of nums except nums[i].
        """

        if len(nums) == 0:
            return []

        result: List[int] = len(nums) * [1]

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        r_product: int = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= r_product
            r_product *= nums[i]

        return result
