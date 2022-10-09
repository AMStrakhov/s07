"""
Description:
Write class for a two-dimensional vector with attributes: x and y.
Implement magic methods for:
 * comparison (__eq__)
 * sum of vectors (__add__)
 * difference between vectors (__sub__)
 * product of a vector and a number (__mul__)
 * quotient of a vector and a number (__truediv__)
 * string representation in format: "Vector (<x>, <y>)"
If an operation is applied between not supported types (like a sum of
a vector and an int, or product of two vectors), raise TypeError exception
wtih a message: "<type> is not supported for this operation."

Examples:
>>> Vector(1, 2) + Vector(-1, 1)
Vector (0, 3)
>>> Vector(1, 2) - Vector(-1, 1)
Vector (2, 1)
>>> Vector(6, 6) / 2
Vector (3.0, 3.0)
>>> Vector(6, 6) * 2
Vector (12, 12)
>>> Vector(1, 2) == Vector(1, 2)
True
"""


class Vector:
    ...


if __name__ == "__main__":
    print(Vector(1, 2) + Vector(-1, 1))
    print(Vector(1, 2) - Vector(-1, 1))
    print(Vector(6, 6) / 2)
    print(Vector(6, 6) * 2)
    print(Vector(1, 2) == Vector(1, 2))
