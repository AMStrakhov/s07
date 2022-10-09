from unittest import TestCase

from problem_04 import Bin


class TestProblem04(TestCase):
    def setUp(self) -> None:
        self.bin_a = Bin("0011")
        self.bin_b = Bin("0101")

    def test_and(self) -> None:
        self.assertEqual(Bin("0001"), self.bin_a & self.bin_b)

    def test_or(self) -> None:
        self.assertEqual(Bin("0111"), self.bin_a | self.bin_b)

    def test_setter(self) -> None:
        value = "1111"
        self.bin_a.value = value
        self.assertEqual(Bin(value), self.bin_a)

    def test_getter(self) -> None:
        value = "1111"
        self.assertIn(value, Bin(int(value, 2)).value)
