from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict_dup = {}
        out = []
        for item in nums:
            if item not in dict_dup.keys():
                dict_dup[item] = None
            else:
                out.append(item) 
        return out

class Solution:        
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        nums.clear()
        return list([i for i in count if count[i] > 1])
    
    
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        """
            Since we have to solve this problem in constant space complexity so the only way is to use the space of given array and manipulate it.
            Since the elements in the array are in range [1..n], we can consider the elements as idexes also and to be precise (element - 1) as it is a 0-indexed array.
            Since we can't use any extra space so let us mark the elements encountered in the given array only. This can be done by multiplying the element with -1.
            Now for each element, we will treat it as the index and check whether the value present at that index is visited or not. If it is visited then it is a duplicate else we mark that element as visited(multiply by -1).
        """
        for num in nums:
            if nums[abs(num) - 1] < 0:
                output.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return output

Solution 2
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
            We can't use an extra hashmap because space complexity has to be O(1).
            So let's use the given array as hashmap based on the logic that the all numbers are in the range of 1-n so we can use the index of array as the numbers (index+1 as 0th index will represent 1) keys of hashmap and the values as the number of occurrences of each number.
            We can achieve the above be decrementing each element by 1 to sustain the nth index as max value of array will be n but max index would be n-1.
            Now we will iterate over the array and will treat each element as the correct index of number.
            Everytime we encounter a number, the value at its correct index will be incremented by n.
            At the end we divide each number by n so that we get the count of each number(index of array) as the values of array.
            Now the elements with value == 2 would be the duplicates.
        """
        n = len(nums)
        nums = [num-1 for num in nums]
        print(nums)
        for num in nums:
            nums[num % n] += n
        # nums = [num//n for num in nums]
        output = []
        for key, num in enumerate(nums):
            if num//n == 2:
                output.append(key+1)
        return output

Solution 3 - Cyclic Sort
class Solution:
    def cyclicSort(self, nums):
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[correct] != nums[i]:
                nums[correct], nums[i] = nums[i], nums[correct]
            else:
                i += 1

    def findDuplicates(self, nums: List[int]) -> List[int]:
        self.cyclicSort(nums)
        output = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                output.append(nums[i])
        return output
