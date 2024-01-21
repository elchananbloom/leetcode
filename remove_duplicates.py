
from typing import List


class RemoveDuplicates:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        # pointer for the current element
        p : int = 0
        
        # iterate through the array
        for i in range(len(nums)):
            # if the current element is not equal to the element at pointer
            if nums[i] != nums[p]:
                # increment the pointer
                p += 1
                # swap the current element with the element at pointer
                nums[i], nums[p] = nums[p], nums[i]
        
        # return the length of the array
        return p + 1
    
    def test(self):
        nums : List[int] = [1,1,2]
        assert(self.removeDuplicates(nums) == 2)
        
        nums : List[int] = [0,0,1,1,1,2,2,3,3,4]
        assert(self.removeDuplicates(nums) == 5)
        
        nums : List[int] = [1,1,1,1,1,1,1,1,1,1]
        assert(self.removeDuplicates(nums) == 1)
        
        nums : List[int] = [1,2,3,4,5,6,7,8,9,10]
        assert(self.removeDuplicates(nums) == 10)
        
        nums : List[int] = [1,1,1,1,1,1,1,1,1,1]
        assert(self.removeDuplicates(nums) == 1)
        
        print('All tests passed!: remove_duplicates.py')