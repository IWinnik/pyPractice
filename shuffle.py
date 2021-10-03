from random import randint

def shuffle(data):
    res = []
    while data:
        lottery = randint(0,len(data)-1)
        res.append(data.pop(lottery))

    return res

print(shuffle([2,3,6,8,9]))