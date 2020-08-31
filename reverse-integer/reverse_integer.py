# Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x: int) -> int:
        test_num = 0
        sign = math.copysign(1, x)
        # print(int(sign))
        # print(x)
        x = abs(x)
        while x > 0:
            remainder = x%10
            test_num = 10 * test_num + remainder
            x = x // 10
        # print(test_num)
        if test_num >= -2147483648 and test_num <= 2147483647:
            return int(sign) * test_num
        else:
            return 0
        
