class Sequence:
    def __init__(self, seq: str):
        self.seq = seq
        self.cur = 0

    def __next__(self):
        if self.cur < len(self):
            current = self.seq[self.cur]
            self.cur += 1
            return current
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.seq)

import pytest

s = Sequence('abcd')
print(list(s))
print(len(s))


s = Sequence('xyz')

print(next(s))
print(next(s))
print(next(s))
with pytest.raises(IndexError):
    print(next(s))