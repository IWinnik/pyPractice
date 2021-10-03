

def reverse(x: int) -> int:
    s = [n for n in str(x)]
    sign = ''
    if s[0] == '-':
        s = s[1:]
        sign = '-'
    s.reverse()
    s = [sign] + s
    res = int(''.join(s))
    if (res > 2 ** 31 - 1) or (res < -2 ** 31):
        return 0
    return res


a = reverse(345)

print(a)