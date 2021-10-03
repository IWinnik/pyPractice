def letters():
    return [chr(a) for a in range(97,123)]

print(letters())


import pytest
AZ = 'abcdefghijklmnopqrstuvwxyz'
assert len(letters()) == 26
assert letters() == [c for c in AZ]
assert AZ not in letters.__code__.co_consts
