from typing import overload


@overload
def hello(s: int) -> int:
    ...


@overload
def hello(s: str) -> str:
    ...


def hello(s):
    if isinstance(s, int):
        return "Got an integer!"
    if isinstance(s, str):
        return "Got a string"
    raise ValueError('You must pass either int or str')


if __name__ == '__main__':
    print(hello(1))
    a = hello(1) + 1
    b = hello(1) + 9
