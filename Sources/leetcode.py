from collections import OrderedDict
from itertools import chain


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def twoSum(arr, target):
    complement = {}
    sol = []
    for x in arr:
        if target - x in complement:
            complement[target - x] += 1
        else:
            complement[target - x] = 1
    for x in set(arr):
        if x in complement and x * 2 != target:
            sol.append([min(x, target-x), max(x, target-x)])
            complement.pop(target-x)
        elif x in complement:
            if complement[x] > 1:
                sol.append([x, x])
                complement.pop(x)
    return sol


def threeSum(nums):
    sol = []
    for x in set(nums):
        if x not in set(chain(*sol)):
            temp = nums[:]
            temp.remove(x)
            for row in twoSum(temp, -x):
                row.append(x)
                sol.append(row)
    return sol


class Solution:
    def jump(self, nums) -> int:
        if len(nums) < 2:
            return 0
        minArr = [float("+inf") for _ in range(len(nums)-1)]
        minArr.append(0)
        for i in range(len(nums) - 2, -1 , - 1):
            minArr[i] = min(minArr[i:min(i+nums[i]+1,len(nums))])+1
        return minArr[0]
        
                    

sol = Solution()
print(sol.jump([2,3,1,1,4]))
