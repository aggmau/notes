"""
Least Memory BST

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def fist_last_function(self, nums, target, firstindex):  # added colon here
        start = 0
        end = len(nums)-1
        intermediate_ans = -1
        while start <= end:
            mid = start + (end-start)//2
            if target < nums[mid]:  # corrected the comparisons to check with nums[mid]
                end = mid - 1
            elif target > nums[mid]:  # corrected the comparisons to check with nums[mid]
                start = mid + 1
            else:
                intermediate_ans = mid
                if firstindex:
                    end = mid - 1
                else:
                    start = mid + 1
        return intermediate_ans
         

    def searchRange(self, nums, target):
        ans = [-1,-1]
        ans[0] = self.fist_last_function(nums, target, True)  # added 'self.' to call instance method
        ans[1] = self.fist_last_function(nums, target, False)  # added 'self.' to call instance method
        return ans



    
