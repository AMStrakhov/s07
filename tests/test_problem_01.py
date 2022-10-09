from unittest import TestCase

from problem_01 import Car


class TestProblem01(TestCase):
    def test_attrs(self) -> None:
        car = Car(brand="x", model="y", max_speed=200)
        attrs = ["brand", "model", "max_speed"]
        for attr in attrs:
            with self.subTest(attr):
                self.assertTrue(hasattr(car, attr))

    def test_miles(self) -> None:
        km = [0, 100, 96, 200]
        miles = [0, 62, 60, 124]
        for max_spd, expected in zip(km, miles):
            car = Car(brand="x", model="y", max_speed=max_spd)
            self.assertEqual(expected, car.max_speed_miles)

    def test_field(self) -> None:
        self.assertEqual(0.62137, Car.km_miles_ratio)

    def test_repr(self) -> None:
        car = Car(brand="X", model="Y", max_speed=299)
        self.assertEqual("X Y (max spd: 299 km/h)", str(car))
