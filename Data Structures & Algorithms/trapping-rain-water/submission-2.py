class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = [0] * len(height)
        water_count = 0
        left.append(height[0])
        for i in range(1,len(height)):
            left.append(max(left[i-1], height[i]))
        right[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            right[i] = max(right[i+1], height[i])
        print(left,right)
        for i in range(len(height)):
            print(height[i],min(left[i], right[i]-height[i]))
            count = min(left[i], right[i])-height[i]
            if count > 0:
                water_count += count
        return water_count