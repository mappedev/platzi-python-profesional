import time
from typing_extensions import Self


class FiboIter:
    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self) -> Self:
        self.a = 0
        self.b = 1
        self.counter = 0
        return self

    def __next__(self) -> int:
        if self.counter >= self.max:
            raise StopIteration

        if self.counter == 0:
            self.counter += 1
            return self.a

        if self.counter == 1:
            self.counter += 1
            return self.b

        result = self.a + self.b
        self.a = self.b
        self.b = result
        self.counter += 1
        return result


def run() -> None:
    fibonacci = FiboIter(2)
    for i in fibonacci:
        print(i)
        time.sleep(1)


if __name__ == "__main__":
    run()
