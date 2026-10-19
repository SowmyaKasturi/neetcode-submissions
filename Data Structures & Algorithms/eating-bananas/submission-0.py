class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        left = 1
        right = max(piles)
        size = len(piles)
        while left < right:
            mid = (right+left) // 2
            t_h = sum(ceil(piles[i]/mid) for i in range(size))
            if t_h > h:
                left = mid + 1
            else:
                right = mid
        return left
        

