"""
Description:
Write a class that operates binary numbers.

It accepts a number in a binary or a decimal format as an argument in __init__.

The number should be stored in a private attribute called `__value` without
direct access from the outer scope as an integer.

It is only allowed to set and get the value using setter (@value.setter) and
getter (@property) in a binary string format (like "10111").

Implement bitwise `AND` (__and__), bitwise `OR` (__or__), equals (__eq__),
and __repr__ methods.

Examples:
>>> Bin("1010") & Bin("1110")
0b1010
>>> Bin("1010") | Bin("1110")
0b1110
>>> Bin("1010") == Bin("1110")
False
"""


class Bin:
    ...


if __name__ == "__main__":
    print(Bin("1010") & Bin("1110"))
    print(Bin("1010") | Bin("1110"))
    print(Bin("1010") == Bin("1110"))
