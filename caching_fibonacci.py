from typing import Callable, Dict


def caching_fibonacci() -> Callable[[int], int]:

    # Store already computed Fibonacci numbers
    cache: Dict[int, int] = {}

    def fibonacci(n: int):
        if n <= 0:  # Base case: fib(0) = 0
            return 0
        if n == 1:  # Base case: fib(1) = 1
            return 1
        if n in cache:
            return cache[n]  # Return cached value if available

        # Compute recursively and store in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci  # Return the function with its cache


if __name__ == "__main__":
    fib = caching_fibonacci()

    print(fib(10))
    print(fib(15))

    assert fib(10) == 55
    assert fib(15) == 610
