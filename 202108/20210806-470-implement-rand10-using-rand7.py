# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        r1 = rand7()
        r2 = rand7()
        r3 = rand7()

        # (r1 - 1) * 7 + (r2 - 1) can randomize all numbers between 0 & 49
        # (7 * 49 + 7) % 10 == 0
        val = r1 + r2 * 3 - r3 + 7

        return val % 10 + 1
