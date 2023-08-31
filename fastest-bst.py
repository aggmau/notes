"""
sample bst with the least runtime
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) -1
        if r < 0:
            return [-1,-1]
        if nums[l] == nums[r]:
            if nums[l] == target:
                return [0, len(nums)-1]
            else:
                return [-1,-1]
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                # Find start
                tl, tr = l, m
                while tl+1 < tr:
                    tm = (tl+tr) // 2
                    if nums[tm] == target:
                        tr = tm
                    else:
                        tl = tm + 1
                ts = tl if nums[tl] == target else tr
                # find end
                tl, tr = m, r
                while tl+1 < tr:
                    tm = (tl+tr) // 2
                    if nums[tm] == target:
                        tl = tm
                    else:
                        tr = tm - 1
                te = tr if nums[tr] == target else tl
                return [ts, te]
        return [-1,-1]
