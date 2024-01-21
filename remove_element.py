
from typing import Any, List


class RemoveElement:
    def removeElement(self, nums: List[Any], val: int) -> int:
        size : int = len(nums)
        pe: int = size - 1
        result : int = size
        for size1 in range(size - 1, -1, -1):
            if nums[size1] == val:
                nums[size1], nums[pe] = nums[pe], '_'
                pe -= 1
                result -= 1
        return result
    
    def test(self):
        nums : List[Any] = [3,2,2,3]
        val : int = 3
        assert(self.removeElement(nums, val) == 2)
        assert(nums == [2,2,'_', '_'])
        
        nums : List[Any] = [0,1,2,2,3,0,4,2]
        val : int = 2
        assert(self.removeElement(nums, val) == 5)
        # assert(nums == [0,1,3,0,4,'_', '_', '_'])
        
        nums : List[Any] = [1]
        val : int = 1
        assert(self.removeElement(nums, val) == 0)
        # assert(nums == ['_'])
        
        nums : List[Any] = [1]
        val : int = 2
        assert(self.removeElement(nums, val) == 1)
        # assert(nums == [1])
        
        print('All tests passed!: remove_element.py')
        
        