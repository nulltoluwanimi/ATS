l = [1, 2, 3, 4]


def loop():
    for num in l:
        yield num


f = loop()
print(next(f), next(f))


# for r in f:
#     print(r)


# new_l = map(lambda i: i**2,l)

class Iter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current >= self.n:
            raise StopIteration
        return self.current
