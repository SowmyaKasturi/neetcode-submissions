class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size= len(heights)
        max_area = 0
        right = [size] * size
        left = [0]*size
        for i in range(size-1,-1,-1):
            p = i + 1
            while p < size and heights[p] >= heights[i]:
                p = right[p]
            right[i] = p

        for i in range(size):
            p = i -1
            while p >=0 and heights[p] >= heights[i]:
                p = left[p]
            left[i] = p

        for i in range(size):
            max_area = max(max_area, heights[i]*(right[i]-left[i]-1))
        return max_area