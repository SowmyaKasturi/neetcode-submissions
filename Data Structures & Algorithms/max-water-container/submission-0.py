class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        area = 0
        for i in range(size-1):
            for j in range(i+1,size):
                area = max(area, min(heights[i],heights[j])*(j-i))
        return area 
