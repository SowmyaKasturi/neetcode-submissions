class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size= len(heights)
        max_area = 0
        for i in range(size):
            height = heights[i]
            left,right = i,i+1
            while right <size and heights[right] >= height:
                right += 1
            while left >=0 and heights[left] >= height:
                left -= 1
            max_area = max(max_area, height*(right-left-1))
        return max_area