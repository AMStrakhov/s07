from unittest import TestCase

from problem_02 import Manager, Programmer, Designer


class TestProblem02(TestCase):
    def test_programmer_work(self) -> None:
        self.assertEqual(
            "code by programmer Mr. X Y", Programmer("X", "Y").work()
        )

    def test_designer_work(self) -> None:
        self.assertEqual(
            "design by designer Mrs. X Y", Designer("X", "Y", True).work()
        )

    def test_manager_work(self) -> None:
        m = Manager("X", "Y")
        self.assertSequenceEqual([], list(m.work()))
        m.subordinates.extend([Programmer("A", "B", True), Designer("C", "D")])
        self.assertSequenceEqual(
            ["code by programmer Mrs. A B", "design by designer Mr. C D"],
            list(m.work()),
        )
