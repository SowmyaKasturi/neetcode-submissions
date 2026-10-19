class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _thash = {}
        for i in nums:
            _thash.setdefault(i,0)
            _thash[i]+= 1
        return [_[0] for _ in sorted(_thash.items(),key=lambda x:x[1], reverse=True)][:k]