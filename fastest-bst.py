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
        # declaring left and right
        l, r = 0, len(nums) -1
        # special condition if array is empty
        if r < 0:
            return [-1,-1]
        # special condition if array consist of same member
        if nums[l] == nums[r]:
            if nums[l] == target:
                return [l, r]
            else:
                return [-1,-1]
        # regular condition
        while l <= r:
            # set middle
            m = (l + r) // 2
            # move search array to left slice
            if nums[m] > target:
                r = m - 1
            # move search array to right slice
            elif nums[m] < target:
                l = m + 1
            # when target found
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
