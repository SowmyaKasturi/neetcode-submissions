class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sum_n = 0
        while n > 0:
            while n > 0:
                rem = n % 10
                sum_n += (rem*rem)
                n //= 10
            if sum_n == 1:
                return True
            if sum_n in seen:
                return False
            seen.add(sum_n)
            n = sum_n
            sum_n = 0