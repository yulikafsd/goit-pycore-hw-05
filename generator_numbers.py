import re
from typing import Callable, Iterator
from decimal import Decimal


def generator_numbers(text: str) -> Iterator[Decimal]:
    # Find all profits in text acc. to a pattern "space nums dot nums space"
    numbers = re.findall(r" (\d+\.\d+) ", text)
    for num in numbers:
        yield Decimal(num)


def sum_profit(text: str, func: Callable):
    # Sum profit to get income
    return sum(func(text))


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
