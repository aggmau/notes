"""
Binary Search Tree

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = self.binary_search_left(nums, target), self.binary_search_right(nums, target)
        return (left, right) if left <= right else [-1, -1]

    def binary_search_left(self, array, target):
        left, right = 0, len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > array[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binary_search_right(self, array, target):
        left, right = 0, len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if target >= array[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
        
