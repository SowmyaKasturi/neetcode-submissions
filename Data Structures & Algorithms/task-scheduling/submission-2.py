from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq_map = Counter(tasks)
        max_freq_heap = [[-val, key] for key, val in task_freq_map.items()]
        heapq.heapify(max_freq_heap)
        
        queue = deque()  # Cooldown queue
        time = 0
        
        while max_freq_heap or queue:
            time += 1  # Time always moves forward
            
            if max_freq_heap:
                freq, task = heapq.heappop(max_freq_heap)
                if freq + 1 < 0:  # More occurrences left
                    queue.append([freq + 1, task, time + n])  # Store next available time
            
            if queue and queue[0][2] <= time:  # Task cooldown done
                heapq.heappush(max_freq_heap, queue.popleft()[:2])  # Push back (freq, task)
        
        return time
