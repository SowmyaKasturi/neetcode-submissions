class MedianFinder:

    def __init__(self):
        self.res = []

    def addNum(self, num: int) -> None:
        if not self.res:
            self.res.append(num)
            return  # Stop further execution

        low, high = 0, len(self.res) - 1

        # Binary search to find the correct position
        while low <= high:
            mid = (high + low) // 2
            if self.res[mid] < num:
                low += 1
            else:
                high -= 1

        # Insert at the correct position
        self.res.insert(low, num)

    def findMedian(self) -> float:
        length = len(self.res)
        if length % 2 == 1:
            return self.res[length // 2]
        else:
            return (self.res[length // 2 - 1] + self.res[length // 2]) / 2
