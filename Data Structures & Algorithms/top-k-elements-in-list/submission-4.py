class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [ i for i, v in sorted(Counter(nums).items() , key=lambda i: i[1], reverse=True)[:k]]