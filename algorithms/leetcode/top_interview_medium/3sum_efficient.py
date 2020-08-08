"""
this should be a faster version

right now, O(n^2 + n) comes to mind, but how exactly does that run?
you produce i,j combination: which is a (i, num_i, j, num_j)
you produce k combo: which is (k, num_k)


"""


def threeSum(nums: List[int]) -> List[List[int]]:
    potential_ks = set(nums)
    
