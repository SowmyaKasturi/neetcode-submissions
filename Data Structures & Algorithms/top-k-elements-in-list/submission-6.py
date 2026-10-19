class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(_[0] for _ in sorted(Counter(nums).items(), key=lambda x:x[1])[::-1])[:k]