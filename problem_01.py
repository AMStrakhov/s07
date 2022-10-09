"""
Description:

Create a class Car with 3 attributes: brand, model, max_speed.
An instance of the Car should be printed in the format:
<brand> <model> (max spd: <max_speed> km/h)

Class should have a property `max_speed_miles`, that returns `max_speed`
attribute value converted in miles (multiplied by 0.62137, and rounded to
an integer. Put 0.62137 into km_miles_ratio field of `Car` class).

Examples:
>>> mazda6 = Car(brand="Mazda", model="6", max_speed=200)
>>> print(mazda6)
Mazda 6 (max spd: 200 km/h)
"""


class Car:
    ...


if __name__ == "__main__":
    mazda6 = Car(brand="Mazda", model="6", max_speed=200)
    print(mazda6)
