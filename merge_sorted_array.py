
from typing import List


class MergerSortedArray:
    # merge two sorted arrays into the first array without using built in functions
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # create a copy of nums1
        nums1_copy : List[int] = nums1[:m]

        # pointers for nums1_copy, nums2, and nums1
        p1 : int = 0
        p2 : int = 0
        p : int = 0

        # compare elements from nums1_copy and nums2 and add the smallest one into nums1
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1
        nums1[p:] = nums1_copy[p1:] if p1 < m else nums2[p2:] if p2 < n else []
    
    def test(self):
        nums1 : List[int] = [1,2,3,0,0,0]
        m : int = 3
        nums2 : List[int] = [2,5,6]
        n : int = 3
        self.merge(nums1, m, nums2, n)
        assert(nums1 == [1,2,2,3,5,6])

        nums1 : List[int] = [1]
        m : int = 1
        nums2 : List[int] = []
        n : int = 0
        self.merge(nums1, m, nums2, n)
        assert(nums1 == [1])

        nums1 : List[int] = [0]
        m : int = 0
        nums2 : List[int] = [1]
        n : int = 1
        self.merge(nums1, m, nums2, n)
        assert(nums1 == [1])
        
        print('All tests passed!: merge_sorted_array.py')