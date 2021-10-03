from typing import List

import pytest

print(list(range(10)))

class chunker:
    def __init__(self, seq, pagesize):
        self.seq = seq
        self.pagesize = pagesize
        self.cursor = 0

    def __next__(self):
        cur_end = self.cursor + self.pagesize
        if cur_end <= len(self.seq):
            current = self.seq[self.cursor:cur_end]
            self.cursor += self.pagesize
            return current
        elif self.cursor < len(self.seq):
            current = self.seq[self.cursor:]
            self.cursor += self.pagesize
            return current
        else:
            raise StopIteration()

pages = chunker(seq=list(range(10)), pagesize=4)
print(next(pages))
print(next(pages))
print(next(pages))
with pytest.raises(StopIteration):
    next(pages)

