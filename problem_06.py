"""
Description:

Write a `@counter` decorator that will display the set of recursive functions
and the number of recursive function calls.

The decorator must create two attributes for the function:
* ncalls — the number of function calls;
* rdepth — recursion depth.
The `ncalls` and `rdepth` counters must be set to zero each time
the recursion is entered.

Examples:
>>> func2(0, 5)
>>> print(func2.ncalls, func2.rdepth)
63 6
>>> func2(0, 3)
>>> print(func2.ncalls, func2.rdepth)
15 4
"""
from typing import Callable


def counter(func: Callable) -> Callable:
    # Write your solution here
    ...


@counter
def func2(n: int, steps: int) -> None:
    if steps == 0:
        return

    func2(n + 1, steps - 1)
    func2(n - 1, steps - 1)


if __name__ == "__main__":
    func2(0, 5)
    print(func2.ncalls, func2.rdepth)
    func2(0, 3)
    print(func2.ncalls, func2.rdepth)
