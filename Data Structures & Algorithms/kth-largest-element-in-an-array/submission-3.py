class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        for num in nums[k:]:
            if num > self.heap[0]:
                heapq.heappushpop(self.heap, num)
        return self.heap[0]
        # def heapify_up(index):
        #     parent = (index-1)//2
        #     while index > 0 and self.heap[parent] < self.heap[index]:
        #         self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
        #         index = parent
        #         parent = (index-1)//2

        # for i in nums:
        #     self.heap.append(i)
        #     heapify_up(len(self.heap)-1)

        # while k > 0 and self.heap:
        #     self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        #     ele = self.heap.pop()
        #     length = len(self.heap)
        #     while length > 0:
        #         heapify_up(length-1)
        #         length -= 1
        #     k -= 1
        # return ele