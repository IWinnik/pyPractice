def countAndSay( n: int) -> str:
    if n == 1:
        return "1"



    a = countAndSay(n-1)
    last_char = a[0]
    counter = 1
    res = ''

    if not a[1:]:
        return str(counter) + last_char
    for char in a[1:]:
        if last_char != char:
            res += str(counter)
            res += last_char
            last_char = char
            counter = 1
        else:
            counter += 1

    res += str(counter) + last_char
    return res

print(countAndSay(4))