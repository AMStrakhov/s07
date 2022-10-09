from unittest import TestCase

from problem_03 import Vector


class TestProblem03(TestCase):
    def setUp(self) -> None:
        self.vector_a = Vector(1, 2)
        self.vector_b = Vector(-2, 4)

    def test_eq(self) -> None:
        self.assertNotEqual(self.vector_a, self.vector_b)

    def test_sum(self) -> None:
        self.assertEqual(Vector(-1, 6), self.vector_a + self.vector_b)

    def test_diff(self) -> None:
        self.assertEqual(Vector(3, -2), self.vector_a - self.vector_b)

    def test_mult(self) -> None:
        multipliers = [0, 1, 2]
        coords_cases = [(0, 0), (1, 2), (2, 4)]
        for coords, multiplier in zip(coords_cases, multipliers):
            with self.subTest(multiplier):
                self.assertEqual(Vector(*coords), self.vector_a * multiplier)

    def test_div(self) -> None:
        self.assertEqual(Vector(0.5, 1), self.vector_a / 2)

    def test_sum_types(self) -> None:
        with self.assertRaises(TypeError) as cm:
            self.vector_a + 2  # noqa
        self.assertEqual(
            "int is not supported for this operation.", str(cm.exception)
        )

    def test_diff_types(self) -> None:
        with self.assertRaises(TypeError) as cm:
            self.vector_a - 2  # noqa
        self.assertEqual(
            "int is not supported for this operation.", str(cm.exception)
        )

    def test_mul_types(self) -> None:
        with self.assertRaises(TypeError) as cm:
            self.vector_a * self.vector_b  # noqa
        self.assertEqual(
            "Vector is not supported for this operation.", str(cm.exception)
        )

    def test_div_types(self) -> None:
        with self.assertRaises(TypeError) as cm:
            self.vector_a / self.vector_b  # noqa
        self.assertEqual(
            "Vector is not supported for this operation.", str(cm.exception)
        )
