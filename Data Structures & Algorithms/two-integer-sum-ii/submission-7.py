class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # complement = {}
        # for i in range(len(numbers)):
        #     if numbers[i] in complement:
        #         return [complement[numbers[i]] + 1, i +1]
        #     complement[target - numbers[i]] = i
        # return [-1,-1]
        low = 0
        high = len(numbers) - 1
        while low <= high:
            temp_sum = numbers[low] + numbers[high]
            if  temp_sum == target:
                return [low+1,high+1]
            if temp_sum >= target:
                high -= 1
            else:
                low += 1
        return [-1,-1]