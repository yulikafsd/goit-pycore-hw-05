from typing import Callable, Dict


def caching_fibonacci() -> Callable[[int], int]:
    cache: Dict[int, int] = {}

    def fibonacci(n: int):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()

    print(fib(10))
    print(fib(15))

    assert fib(10) == 55
    assert fib(15) == 610
