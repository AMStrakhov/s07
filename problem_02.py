"""
Description:

You have an abstract base class `Employee`.
Create classes inherited from `Employee`:
Employee -> Manager
         -> Programmer
         -> Designer

Every manager has a list of subordinates — special attribute to store
the instances of other employees.

Every employee can work. But results of their work are different:
 * programmers should return string "code by <Employee>"
 (<Employee> is a string representation of the instance)
 * designers should return string "design by <Employee>"
 * and managers should make other employees work: they iterate through the list
 of their subordinates, call their `work()` methods and return a list of
 results.

Examples:
>>> manager = Manager("John", "Smith")
>>> programmer_1 = Programmer("Ada", "Lovelace", True)
>>> programmer_2 = Programmer("Guido", "van Rossum")
>>> designer_1 = Designer("Johny", "Ive")
>>> manager.subordinates.extend([programmer_1, programmer_2, designer_1])
>>> print(list(manager.work()))
[
  'code by programmer Mrs. Ada Lovelace',
  'code by programmer Mr. Guido van Rossum',
  'design by designer Mr. Johny Ive'
]
"""

from abc import ABC


class Employee(ABC):
    position: str = "employee"

    def __init__(
        self, name: str, surname: str, is_female: bool = False
    ) -> None:
        self.name = name
        self.surname = surname
        self._is_female = is_female

    @property
    def _prefix(self) -> str:
        return "Mrs." if self._is_female else "Mr."

    def __repr__(self) -> str:
        return f"{self.position} {self._prefix} {self.name} {self.surname}"

    def work(self) -> str:
        raise NotImplementedError()


if __name__ == "__main__":
    manager = Manager("John", "Smith")
    programmer_1 = Programmer("Ada", "Lovelace", True)
    programmer_2 = Programmer("Guido", "van Rossum")
    designer_1 = Designer("Johny", "Ive")
    manager.subordinates.extend([programmer_1, programmer_2, designer_1])
    print(list(manager.work()))
