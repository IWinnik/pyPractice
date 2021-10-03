def running_tot(seq):
    cur = 0
    res = []
    for i in seq:
        cur = cur + i
        res.append(cur)

    return  res

print(running_tot([-1, 5, -2, 3]))

