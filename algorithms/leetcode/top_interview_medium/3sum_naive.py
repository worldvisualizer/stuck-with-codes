from typing import List

"""
free thinking:

three tries over the loop makes sense to me. index i < j < k will iterate,
because those are three unique elements for the solution.
- iterative solution looks fine: no overlapping set space
- i + j == -k, or i + k == -j, or j + k == -i

expected runtime O(n^3 * n^3 (for duplicate check)) 

is there a better way? we have n number of k. 
"""
def three_are_sum(i, j, k):
    return i + j == -1 * k or i + k == -1 * j or j + k == -1 * i


def check_duplicate(result, three_sums):
    str_result = [str(elem) for elem in result]
    return str(three_sums) not in str_result


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    length = len(nums)
    for i in range(0, length-2):
        for j in range(i + 1, length-1):
            for k in range(j + 1, length):
                num_i, num_j, num_k = nums[i], nums[j], nums[k]
                three_nums = sorted([num_i, num_j, num_k])
                if three_are_sum(num_i, num_j, num_k) and check_duplicate(result, three_nums):
                    result.append(three_nums)
    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([3,-2,1,0]))
