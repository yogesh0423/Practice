class Solution:
    def climbStairs(self, n):
        previous2 = 1
        previous1 = 1

        for _ in range(2, n + 1):
            current = previous1 + previous2
            previous2 = previous1
            previous1 = current

        return previous1
