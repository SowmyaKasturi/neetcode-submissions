class TimeMap:
    from collections import OrderedDict
    def __init__(self):
        self.key_value_store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.key_value_store.get(key):
            self.key_value_store[key] = OrderedDict({timestamp: value})
        else:
            self.key_value_store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        def binary_search(timestamps, ts):
            low = 0
            high = len(timestamps) - 1
            bestmatch = 0
            if low == high and timestamps[0] < ts:
                return timestamps[0]

            while low <= high:
                mid = (high+low) // 2
                if timestamps[mid] < ts:
                    bestmatch = timestamps[mid]
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return bestmatch or ""
            
        if key in self.key_value_store:
            if timestamp in self.key_value_store[key]:
                return self.key_value_store[key][timestamp]
            else:
                timestamps = list(self.key_value_store[key].keys())
                value = binary_search(timestamps, timestamp)
                return self.key_value_store[key][value] if value else ""
        return ""