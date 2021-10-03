int_32_bit = 2 ** 31


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign_flag = False

        if len(s) == 0:
            return 0

        if s[0] == "-":
            sign_flag = True

        if s[0] == "-" or s[0] == "+":
            s = s[1:]

        if len(s) == 0:
            return 0

        if not s[0].isdigit():
            return 0
        temp_s = []
        for char in s:
            if char.isdigit():
                temp_s.append(char)
            else:
                break

        # filtered_obj = filter(isdigit_or_dot, s)
        filtered_s = ''.join(temp_s)

        res = int(filtered_s)
        if sign_flag:
            res = res * -1

        if res >= int_32_bit:
            return int_32_bit - 1

        if res < -int_32_bit:
            return -int_32_bit

        return res