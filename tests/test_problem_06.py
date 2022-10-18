from unittest import TestCase

from problem_06 import counter, func2


@counter
def func1(steps: int) -> None:
    if steps == 0:
        return
    func1(steps - 1)


class TestProblem06(TestCase):
    def test_ncalls(self) -> None:
        cases = [(0, 1), (1, 3), (2, 7), (3, 15)]
        for steps, ncalls in cases:
            with self.subTest(steps):
                func2(0, steps)
                self.assertEqual(ncalls, func2.ncalls)

    def test_ncalls_single(self) -> None:
        cases = [(0, 1), (1, 2), (2, 3), (3, 4)]
        for steps, ncalls in cases:
            with self.subTest(steps):
                func1(steps)
                self.assertEqual(ncalls, func1.ncalls)

    def test_rdepth(self) -> None:
        cases = [(0, 1), (1, 2), (2, 3), (3, 4)]
        for steps, rdepth in cases:
            with self.subTest(steps):
                func2(0, steps)
                self.assertEqual(rdepth, func2.rdepth)

    def test_rdepth_single(self) -> None:
        cases = [(0, 1), (1, 2), (2, 3), (3, 4)]
        for steps, rdepth in cases:
            with self.subTest(steps):
                func1(steps)
                self.assertEqual(rdepth, func1.rdepth)
